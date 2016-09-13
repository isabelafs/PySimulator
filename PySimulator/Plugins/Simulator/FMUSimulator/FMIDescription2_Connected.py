#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (C) 2011-2015 German Aerospace Center DLR
(Deutsches Zentrum fuer Luft- und Raumfahrt e.V.),
Institute of System Dynamics and Control
Copyright (C) 2014-2015 Open Source Modelica Consortium
All rights reserved.

This file is part of PySimulator.

PySimulator is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySimulator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PySimulator. If not, see www.gnu.org/licenses.
'''
import Plugins.Analysis.FMU.StronglyConnected as StronglyConnected
import xml.etree.ElementTree as ET
import collections

class FMIDescription:
    ''' This object holds the description of an Functional Mock-up Interface for Model Exchange
        It parses an XML-file description as defined by FMI Version 2.0
        The model description (FMI) is usually part of a Functional Mock-Up Unit (FMU)
    '''
    def __init__(self, FMUInterfaces,xml):
        ''' Create FMIDescription from XML-file
            @param xmlFile: File object of the describing XML-Document
        '''
        self.FMUInterfaces = FMUInterfaces
        self.xml=xml
        ''' initialization of variables and more visible public interface '''
        self.me = None
        self.cs = None
        self.defaultStartTime = None
        self.defaultStopTime = None
        self.defaultTolerance = None
        self.defaultStepSize = None
        self.scalarVariables = collections.OrderedDict()
        self.ValueReference ={}
        self.fmiVersion = None
        self.modelName = None
        self.guid = None
        self.description = None
        self.author = None
        self.version = None
        self.copyright = None
        self.license = None
        self.generationTool = None
        self.generationDateAndTime = None
        self.variableNamingConvention = 'flat'
        #self.numberOfEventIndicators = None
        self.numberOfEventIndicators = 0
        self.numberOfContinuousStates = 0
        self.internaldependencyorder=None
        self.intializeunknowndependencyorder=None
        self.initializeunknownconnectioninfo={}
        self.connectioninfo={}
        self.variableid={}
        self.inputvarlist=[]
        self.outputvarlist=[]
        
        ## store the variablelist of each fmu with ids to get correct order of evaluation from tarjan
        for key, FMUInterfaceObj in self.FMUInterfaces.iteritems():
            description = FMUInterfaceObj.description
            varlist=description.scalarVariables.keys()
            for v in xrange(len(varlist)):
                name=FMUInterfaceObj.instanceName +'.'+varlist[v]
                self.variableid[name]=key+str(v)
                
        ## Create connection graph combining internal and  external dependency from xml
        root = ET.fromstring(xml)
        graphlist={}
        initialunknowngraphlist={}
        for connection in root.iter('connection'):           
            ## add from and to info with real fmus name and variables
            fromfmuvar=connection.get('fromFmuName')+'.'+connection.get('fromVariableName')
            tofmuvar=connection.get('toFmuName')+'.'+connection.get('toVariableName')         
            ## add from and to info with fmus id 
            fromid=self.variableid[fromfmuvar]
            toid=self.variableid[tofmuvar]           
            ## add connection information with fmus names which will be used in connection resolve           
            key1=self.connectioninfo.has_key(fromfmuvar)
            if (key1==True):
                self.connectioninfo[fromfmuvar].append(tofmuvar)
            else:
                self.connectioninfo[fromfmuvar] = [tofmuvar]
            ## add connection information with fmus id which will be used to get correct order of evaluation from tarjan
            key2=graphlist.has_key(fromid)
            if (key2==True):
                graphlist[fromid].append(toid)
            else:
                graphlist[fromid] = [toid]
            
            ## add connection information with fmus names for initial unknowns           
            key3=self.initializeunknownconnectioninfo.has_key(fromfmuvar)
            if (key3==True):
                self.initializeunknownconnectioninfo[fromfmuvar].append(tofmuvar)
            else:
                self.initializeunknownconnectioninfo[fromfmuvar] = [tofmuvar]
                
            ## add connection information with fmus id for initial unknowns 
            key4=initialunknowngraphlist.has_key(fromid)
            if (key4==True):
                initialunknowngraphlist[fromid].append(toid)
            else:
                initialunknowngraphlist[fromid] = [toid]
            
        for key, FMUInterfaceObj in self.FMUInterfaces.iteritems():
            description = FMUInterfaceObj.description

            self.me = description.me
            self.cs = description.cs
            self.defaultStartTime = description.defaultStartTime
            self.defaultStopTime = description.defaultStopTime
            self.defaultTolerance = description.defaultTolerance
            self.defaultStepSize = description.defaultStepSize

            self.fmiVersion = description.fmiVersion
            self.modelName = description.modelName
            self.guid = description.guid
            self.description = description.description
            self.author = description.author
            self.version = description.version
            self.copyright = description.copyright
            self.license = description.license
            self.generationTool = description.generationTool
            self.generationDateAndTime = description.generationDateAndTime
            self.variableNamingConvention = description.variableNamingConvention
            self.numberOfEventIndicators += int(description.numberOfEventIndicators)
            self.numberOfContinuousStates += description.numberOfContinuousStates
            modelstructure=description.modelStructure
            
            ## get the internaldependency information
            varlist=description.scalarVariables.keys()
            ModelStructureOutputdependency(varlist,modelstructure,graphlist,FMUInterfaceObj,self.connectioninfo,self.variableid)
            ModelStructureInitialUnknowndependency(varlist,modelstructure,initialunknowngraphlist,FMUInterfaceObj,self.initializeunknownconnectioninfo,self.variableid)
              
            outvarlist=[]
            othervarlist=[]           
            for scalarName, var in description.scalarVariables.iteritems():                                
                ## for worst case scenario when no output dependency is provided in xml, assume output depends on all variables
                if(len(modelstructure.outputs)==0):                
                    if(description.scalarVariables[scalarName].causality=="output"):
                        outvar = FMUInterfaceObj.instanceName + '.' + scalarName
                        outvarlist.append(outvar)
                    else:
                        othervar = FMUInterfaceObj.instanceName + '.' + scalarName
                        othervarlist.append(othervar)
                
                ## list items to identify input variables of each fmus
                if(description.scalarVariables[scalarName].causality=="input"):
                        inputvar = FMUInterfaceObj.instanceName + '.' + scalarName
                        self.inputvarlist.append(inputvar)
                                                       
                ## list items to identify output variables of each fmus       
                if(description.scalarVariables[scalarName].causality=="output"):
                        outputvar = FMUInterfaceObj.instanceName + '.' + scalarName
                        self.outputvarlist.append(outputvar)
                            
                if (scalarName.startswith("der(")):
                    scalarName = "der(" + FMUInterfaceObj.instanceName + '.' + scalarName[4:]
                else:
                    scalarName = FMUInterfaceObj.instanceName + '.' + scalarName
                var.valueReference = key + var.valueReference
                self.scalarVariables[scalarName] = var
                self.ValueReference[var.valueReference]=scalarName
            
            ## This loop will be used for worst case scenario when no output dependency is provided in xml, and to create graph information
            for k in xrange(len(othervarlist)):
                fromname=othervarlist[k]
                fromid=self.variableid[fromname]
                for m in xrange(len(outvarlist)):
                    toname=outvarlist[m]
                    toid=self.variableid[toname]
                    ## add connection information with fmus names
                    key7=self.connectioninfo.has_key(fromname)
                    if (key7==True):
                        self.connectioninfo[fromname].append(toname)
                    else:
                        self.connectioninfo[fromname] = [toname]                    
                    ## add connection information with fmus id which will be used to get correct order of evaluation from tarjan
                    key8=graphlist.has_key(fromid)
                    if (key8==True):
                        graphlist[fromid].append(toid)
                    else:
                        graphlist[fromid] = [toid]
        
        scc=StronglyConnected.StronglyConnectedComponents(graphlist)
        unknownscc=StronglyConnected.StronglyConnectedComponents(initialunknowngraphlist)              
        ## create the ordered list with fmunames+variables matching the fmuids        
        orderedlist=[]
        for z in xrange(len(scc)):          
            var=scc[z]
            if(len(var)==1):
                val=var[0]
                fmuname=self.variableid.keys()[self.variableid.values().index(val)]
                orderedlist.append((fmuname,))
            else:
                l=[]
                var=var[::-1]
                for k in xrange(len(var)):
                    val=var[k]
                    fmuname=self.variableid.keys()[self.variableid.values().index(val)]
                    l.append(fmuname)
                orderedlist.append(tuple(l))
        self.internaldependencyorder=orderedlist
        
        ## create the ordered list for initial unknown depedencv with fmunames+variables matching the fmuids        
        unknownorderedlist=[]
        for z in xrange(len(unknownscc)):          
            var=unknownscc[z]
            if(len(var)==1):
                val=var[0]
                fmuname=self.variableid.keys()[self.variableid.values().index(val)]
                unknownorderedlist.append((fmuname,))
            else:
                l=[]
                var=var[::-1]
                for k in xrange(len(var)):
                    val=var[k]
                    fmuname=self.variableid.keys()[self.variableid.values().index(val)]
                    l.append(fmuname)
                unknownorderedlist.append(tuple(l))
                
        self.internaldependencyorder=orderedlist
        self.intializeunknowndependencyorder=unknownorderedlist


def ModelStructureOutputdependency(varlist,modelstructure,graphlist,FMUInterfaceObj,connectioninfo,variableid):
    ## Handle internal connection dependency for outputs of modelstructure
    for i in xrange(len(modelstructure.outputs)):
        outputindex=modelstructure.outputs[i].index
        inputindex=modelstructure.outputs[i].dependencies
        outvar=varlist[int(outputindex)-1]
        toconnection=FMUInterfaceObj.instanceName + '.' + outvar
        #toconnection_id=fmuitems[FMUInterfaceObj.instanceName]+outvar
        toconnection_id=variableid[toconnection]       
        if (inputindex!=''):
            val=inputindex.split()
            for z in xrange(len(val)):
                v1=val[z]
                invar=varlist[int(v1)-1]
                fromconnection=(FMUInterfaceObj.instanceName)+ '.' + invar
                #fromconnection_id=fmuitems[FMUInterfaceObj.instanceName]+invar
                fromconnection_id=variableid[fromconnection]
                ## add connection info with fmus id for correct order of evaluation from tarjan
                key9=graphlist.has_key(fromconnection_id)
                if (key9==True):
                    graphlist[fromconnection_id].append(toconnection_id)
                else:
                    graphlist[fromconnection_id] = [toconnection_id]
               
                ## add connection info with fmunames which will be used for connection resolve
                key10=connectioninfo.has_key(fromconnection)
                if (key10==True):
                    connectioninfo[fromconnection].append(toconnection)
                else:
                    connectioninfo[fromconnection] = [toconnection]


def ModelStructureInitialUnknowndependency(varlist,modelstructure,unknowngraphlist,FMUInterfaceObj,unknownconnectioninfo,variableid):
    ## Handle internal connection dependency for outputs of modelstructure
    for i in xrange(len(modelstructure.initialUnknowns)):
        outputindex=modelstructure.initialUnknowns[i].index
        inputindex=modelstructure.initialUnknowns[i].dependencies
        outvar=varlist[int(outputindex)-1]
        toconnection=FMUInterfaceObj.instanceName + '.' + outvar
        #toconnection_id=fmuitems[FMUInterfaceObj.instanceName]+outvar
        toconnection_id=variableid[toconnection]       
        if (inputindex!=''):
            val=inputindex.split()
            for z in xrange(len(val)):
                v1=val[z]
                invar=varlist[int(v1)-1]
                fromconnection=(FMUInterfaceObj.instanceName)+ '.' + invar
                #fromconnection_id=fmuitems[FMUInterfaceObj.instanceName]+invar
                fromconnection_id=variableid[fromconnection]
                ## add connection info with fmus id for correct order of evaluation from tarjan
                key11=unknowngraphlist.has_key(fromconnection_id)
                if (key11==True):
                    unknowngraphlist[fromconnection_id].append(toconnection_id)
                else:
                    unknowngraphlist[fromconnection_id] = [toconnection_id]
               
                ## add connection info with fmunames which will be used for connection resolve
                key12=unknownconnectioninfo.has_key(fromconnection)
                if (key12==True):
                    unknownconnectioninfo[fromconnection].append(toconnection)
                else:
                    unknownconnectioninfo[fromconnection] = [toconnection]                    

