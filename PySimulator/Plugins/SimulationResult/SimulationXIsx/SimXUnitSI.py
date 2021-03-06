#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (C) 2014 ITI GmbH
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

unitSI = dict()
unitSI['AbsoluteActivity'] = u'1'
unitSI['AbsolutePressure'] = u'Pa'
unitSI['AbsorbedDose'] = u'Gy'
unitSI['AbsorbedDoseRate'] = u'Gy/s'
unitSI['AbsTemp'] = u'K'
unitSI['Accel'] = u'm/s²'
unitSI['Acceleration'] = u'm/s²'
unitSI['AcceptorIonizationEnergy'] = u'eV'
unitSI['AcceptorNumberDensity'] = u'm-3'
unitSI['AcousticAbsorptionCoefficient'] = u'1'
unitSI['AcousticAdmittance'] = u'(m³/s)/Pa'
unitSI['AcousticCompliance'] = u'm³/Pa'
unitSI['AcousticImpedance'] = u'Pa/(m³/s)'
unitSI['AcousticMass'] = u'kg/m^4'
unitSI['ActivationEnergy'] = u'eV'
unitSI['ActivePower'] = u'W'
unitSI['Activity'] = u'Bq'
unitSI['ActivityCoefficient'] = u'1'
unitSI['ActivityCoefficientOfSolute'] = u'1'
unitSI['ActivityOfSolute'] = u'1'
unitSI['ActivityOfSolvent'] = u'1'
unitSI['Admittance'] = u'S'
unitSI['Affinity'] = u'J/mol'
unitSI['AlfvenNumber'] = u'1'
unitSI['AlphaDisintegrationEnergy'] = u'J'
unitSI['AmountOfSubstance'] = u'mol'
unitSI['AmplCurrentContr'] = u'A/(rad/s)'
unitSI['AmplitudeLevelDifference'] = u'dB'
unitSI['Angle'] = u'rad'
unitSI['AngularAcceleration'] = u'rad/s²'
unitSI['AngularCrossSection'] = u'm2/sr'
unitSI['AngularFrequency'] = u'rad/s'
unitSI['AngularImpulse'] = u'Nms'
unitSI['AngularImpulseFlowRate'] = u'Nm'
unitSI['AngularMomentum'] = u'Nms'
unitSI['AngularMomentumFlux'] = u'Nm'
unitSI['AngularVelocity'] = u'rad/s'
unitSI['ApparentPower'] = u'VA'
unitSI['Area'] = u'm²'
unitSI['AreaPDisplChange'] = u'm²/m'
unitSI['AtomicAttenuationCoefficient'] = u'm2'
unitSI['AtomicMassConstant'] = u'kg'
unitSI['AttenuationCoefficient'] = u'm-1'
unitSI['BEConst'] = u'Vs/rad'
unitSI['Beta'] = u'1/Pa'
unitSI['BetaDisintegrationEnergy'] = u'J'
unitSI['Beta_h'] = u'm³/J'
unitSI['Beta_p'] = u'm³/(kg·Pa)'
unitSI['BindingFraction'] = u'1'
unitSI['BiotNumber'] = u'1'
unitSI['BohrMagneton'] = u'A.m2'
unitSI['BraggAngle'] = u'rad'
unitSI['Breadth'] = u'm'
unitSI['BulkModulus'] = u'Pa'
unitSI['CAccFeedbackGain'] = u'A/(m/s²)'
unitSI['CanonicalPartitionFunction'] = u'1'
unitSI['Capacitance'] = u'F'
unitSI['CapacitancePerArea'] = u'F/m2'
unitSI['CapacityFactor'] = u'(rad/s)/Nm^0.5'
unitSI['CarrierLifeTime'] = u's'
unitSI['Charge'] = u'C'
unitSI['ChargeAging'] = u'1/(A.s)'
unitSI['ChargeNumberOfIon'] = u'1'
unitSI['ChemicalPotential'] = u'J/mol'
unitSI['ChromaticityCoordinates'] = u'1'
unitSI['CIESpectralTristimulusValues'] = u'1'
unitSI['CircularWavenumber'] = u'm-1'
unitSI['CircularWaveNumber'] = u'rad/m'
unitSI['CoefficientOfFriction'] = u'1'
unitSI['CoefficientOfHeatTransfer'] = u'W/(m2.K)'
unitSI['CoherenceLength'] = u'm'
unitSI['Compressibility'] = u'1/Pa'
unitSI['ComptonWavelength'] = u'm'
unitSI['Concentration'] = u'mol/m3'
unitSI['Conductance'] = u'1/Ohm'
unitSI['Conductivity'] = u'S/m'
unitSI['ConstC'] = u's/m'
unitSI['ConvCoeff'] = u'W/(m²·K)'
unitSI['CouplingCoefficient'] = u'1'
unitSI['CowlingNumber'] = u'1'
unitSI['CPosFeedbackGain'] = u'A/m'
unitSI['CPressFeedbackGain'] = u'A/Pa'
unitSI['CROCPressFeedbackGain'] = u'A/(Pa/s)'
unitSI['CrossSection'] = u'm²'
unitSI['CRotAccFeedbackGain'] = u'A/(rad/s²)'
unitSI['CRotAngleFeedbackGain'] = u'A/rad'
unitSI['CRotVeloFeedbackGain'] = u'A/(rad/s)'
unitSI['CubicExpansionCoefficient'] = u'1/K'
unitSI['CurieTemperature'] = u'K'
unitSI['Current'] = u'A'
unitSI['CurrentDensity'] = u'A/m2'
unitSI['CurrentDensityOfParticles'] = u'm-2.s-1'
unitSI['CurrentLinkage'] = u'A'
unitSI['CurrentSlope'] = u'A/s'
unitSI['CurvatureVel'] = u'1/m/s'
unitSI['CVeloFeedbackGain'] = u'A/(m/s)'
unitSI['CyclotronAngularFrequency'] = u's-1'
unitSI['Damping'] = u'1/s'
unitSI['DampingCoefficient'] = u's-1'
unitSI['DampingperArea'] = u'Ns/m/m²'
unitSI['DataRate'] = u'bit/s'
unitSI['DataWith'] = u'bit'
unitSI['DebyeCircularFrequency'] = u's-1'
unitSI['DebyeCircularWavenumber'] = u'm-1'
unitSI['DebyeTemperature'] = u'K'
unitSI['DebyeWallerFactor'] = u'1'
unitSI['DecayConstant'] = u's-1'
unitSI['DegreeOfDissociation'] = u'1'
unitSI['Density'] = u'kg/m³'
unitSI['DensityChangeRate'] = u'kg/(m³·s)'
unitSI['DensityOfHeatFlowRate'] = u'W/m2'
unitSI['DensityOfStates'] = u'J-1/m-3'
unitSI['DerDensityByEnthalpy'] = u'kg.s2/m5'
unitSI['DerDensityByPressure'] = u's2/m2'
unitSI['DerDensityByTemperature'] = u'kg/(m3.K)'
unitSI['DerEnergyByDensity'] = u'J.m3/kg'
unitSI['DerEnergyByPressure'] = u'J.m.s2/kg'
unitSI['DerEnthalpyByPressure'] = u'J.m.s2/kg2'
unitSI['DerPressureByDensity'] = u'Pa.m3/kg'
unitSI['DerPressureByTemperature'] = u'Pa/K'
unitSI['Diameter'] = u'm'
unitSI['DiffusionArea'] = u'm²'
unitSI['DiffusionCoefficient'] = u'm2/s'
unitSI['DiffusionLength'] = u'm'
unitSI['DirectionalSpectralEmissivity'] = u'1'
unitSI['Displace'] = u'm'
unitSI['DissipationCoefficient'] = u'1'
unitSI['Distance'] = u'm'
unitSI['dmp_dp'] = u'(kg/s)/Pa'
unitSI['DonorIonizationEnergy'] = u'eV'
unitSI['DonorNumberDensity'] = u'm-3'
unitSI['DoseEquivalent'] = u'Sv'
unitSI['Duration'] = u's'
unitSI['DynamicViscosity'] = u'Pa.s'
unitSI['DynVisc'] = u'Pa·s'
unitSI['Echarge'] = u'C'
unitSI['EffectiveMass'] = u'kg'
unitSI['Efficiency'] = u'1'
unitSI['EFieldStrength'] = u'V/m'
unitSI['ElastCoeff'] = u'm²/N'
unitSI['ElectricalForceConstant'] = u'N/A'
unitSI['ElectricalTorqueConstant'] = u'Nm/A'
unitSI['ElectricCharge'] = u'C'
unitSI['ElectricCurrent'] = u'A'
unitSI['ElectricDipoleMoment'] = u'C.m'
unitSI['ElectricDipoleMomentOfMolecule'] = u'C.m'
unitSI['ElectricFieldStrength'] = u'V/m'
unitSI['ElectricFlux'] = u'C'
unitSI['ElectricFluxDensity'] = u'C/m2'
unitSI['ElectricPolarizabilityOfAMolecule'] = u'C.m2/V'
unitSI['ElectricPolarization'] = u'C/m2'
unitSI['ElectricPotential'] = u'V'
unitSI['ElectricSusceptibility'] = u'1'
unitSI['Electrization'] = u'V/m'
unitSI['ElectrolyticConductivity'] = u'S/m'
unitSI['ElectromagneticEnergyDensity'] = u'J/m3'
unitSI['ElectromagneticMoment'] = u'A.m2'
unitSI['ElectromotiveForce'] = u'V'
unitSI['ElectronNumberDensity'] = u'm-3'
unitSI['ElectronRadius'] = u'm'
unitSI['ElementaryCharge'] = u'C'
unitSI['Emissivity'] = u'1'
unitSI['EModul'] = u'Pa'
unitSI['Energy'] = u'J'
unitSI['EnergyDensity'] = u'J/m3'
unitSI['EnergyFlowRate'] = u'W'
unitSI['EnergyFluence'] = u'J/m2'
unitSI['EnergyFluenceRate'] = u'W/m2'
unitSI['EnergyImparted'] = u'J'
unitSI['Enthalpy'] = u'J'
unitSI['EnthalpyFlow'] = u'J/s'
unitSI['EnthalpyFlowRate'] = u'W'
unitSI['Entropy'] = u'J/K'
unitSI['EntropyFlowRate'] = u'J/(K.s)'
unitSI['EquBulkMod'] = u'Pa'
unitSI['EquivalentAbsorptionArea'] = u'm²'
unitSI['EulerNumber'] = u'1'
unitSI['ExchangeIntegral'] = u'eV'
unitSI['Exposure'] = u'C/kg'
unitSI['ExposureRate'] = u'C/(kg.s)'
unitSI['FaradayConstant'] = u'C/mol'
unitSI['FastFissionFactor'] = u'1'
unitSI['FermiCircularWavenumber'] = u'm-1'
unitSI['FermiEnergy'] = u'eV'
unitSI['FermiTemperature'] = u'K'
unitSI['Flow'] = u'm³/s'
unitSI['FlowDensity'] = u'kg/m²/s'
unitSI['FlowPDisplChange'] = u'(m³/s)/m'
unitSI['FlowPRelChanging'] = u'(m³/s)/-'
unitSI['FluxiodQuantum'] = u'Wb'
unitSI['Force'] = u'N'
unitSI['ForceConst'] = u'N/A'
unitSI['ForcePPressChange'] = u'N/Pa'
unitSI['FourierNumber'] = u'1'
unitSI['FourierNumberOfMassTransfer'] = u'1'
unitSI['Frequency'] = u'Hz'
unitSI['FroudeNumber'] = u'1'
unitSI['FuelConsumption'] = u'kg/Ws'
unitSI['Fugacity'] = u'Pa'
unitSI['Gamma'] = u'1/K'
unitSI['GapEnergy'] = u'eV'
unitSI['GasConst'] = u'J/(kg·K)'
unitSI['GFactorOfAtom'] = u'1'
unitSI['GFactorOfNucleus'] = u'1'
unitSI['GibbsFreeEnergy'] = u'J'
unitSI['Gradient'] = u'1/s'
unitSI['GrandCanonicalPartitionFunction'] = u'1'
unitSI['GrashofNum'] = u'1/K'
unitSI['GrashofNumber'] = u'1'
unitSI['GrashofNumberOfMassTransfer'] = u'1'
unitSI['GrueneisenParameter'] = u'1'
unitSI['GyromagneticCoefficient'] = u'A.m2/(J.s)'
unitSI['HalfLife'] = u's'
unitSI['HalfThickness'] = u'm'
unitSI['HallCoefficient'] = u'm3/C'
unitSI['HartmannNumber'] = u'1'
unitSI['HartreeEnergy'] = u'J'
unitSI['Heat'] = u'J'
unitSI['HeatCapacity'] = u'J/K'
unitSI['HeatCapacityDeriv'] = u'W/K'
unitSI['HeatCond'] = u'W/K'
unitSI['HeatConduct'] = u'W/K'
unitSI['HeatFlow'] = u'W'
unitSI['HeatFlowPerKevin4'] = u'W/K^4'
unitSI['HeatFlowRate'] = u'W'
unitSI['HeatFlowSurf'] = u'W/m²'
unitSI['HeatFlux'] = u'W/m2'
unitSI['HeatRate'] = u'J/Ws'
unitSI['HeatResist'] = u'K/W'
unitSI['HeatTransmCoeff'] = u'W/(m²·K)'
unitSI['Height'] = u'm'
unitSI['HelmholtzFreeEnergy'] = u'J'
unitSI['HoleNumberDensity'] = u'm-3'
unitSI['HydrCapacity'] = u'm³/Pa'
unitSI['HydrConduct'] = u'(m³/s)/Pa'
unitSI['HydrInduct'] = u'kg/(m^4)'
unitSI['Illuminance'] = u'lx'
unitSI['Impedance'] = u'Ohm'
unitSI['Impulse'] = u'N.s'
unitSI['ImpulseFlowRate'] = u'N'
unitSI['Inductance'] = u'H'
unitSI['Inertia'] = u'kgm²'
unitSI['InstantaneousPower'] = u'W'
unitSI['IntegrAmplGain'] = u'(A/s)/V'
unitSI['InternalEnergy'] = u'J'
unitSI['IntrinsicNumberDensity'] = u'm-3'
unitSI['InversePotential'] = u'1/V'
unitSI['InverseVoltage'] = u'1/V'
unitSI['IonicStrength'] = u'mol/kg'
unitSI['IonNumberDensity'] = u'm-3'
unitSI['Irradiance'] = u'W/m2'
unitSI['IsentropicCompressibility'] = u'1/Pa'
unitSI['IsentropicExponent'] = u'1'
unitSI['IsothermalCompressibility'] = u'1/Pa'
unitSI['Kerma'] = u'Gy'
unitSI['KermaRate'] = u'Gy/s'
unitSI['KinematicViscosity'] = u'm2/s'
unitSI['KineticEnergy'] = u'J'
unitSI['KinVisc'] = u'm²/s'
unitSI['KnudsenNumber'] = u'1'
unitSI['KvFactor'] = u'm³/s'
unitSI['LandauGinzburgParameter'] = u'1'
unitSI['LarmorAngularFrequency'] = u's-1'
unitSI['LeakageCoefficient'] = u'1'
unitSI['Length'] = u'm'
unitSI['Lethargy'] = u'1'
unitSI['LevelWidth'] = u'J'
unitSI['LewisNumber'] = u'1'
unitSI['LightExposure'] = u'lx.s'
unitSI['LinDamping'] = u'Ns/m'
unitSI['LinearAbsorptionCoefficient'] = u'm-1'
unitSI['LinearAttenuationCoefficient'] = u'm-1'
unitSI['LinearCurrentDensity'] = u'A/m'
unitSI['LinearDensity'] = u'kg/m'
unitSI['LinearEnergyTransfer'] = u'J/m'
unitSI['LinearExpansionCoefficient'] = u'1/K'
unitSI['LinearIonization'] = u'm-1'
unitSI['LinearStrain'] = u'1'
unitSI['LinearTemperatureCoefficient'] = u'1/K'
unitSI['LineCapacitance'] = u'F/m'
unitSI['LineConductance'] = u'1/(Ohm·m)'
unitSI['LineInductance'] = u'H/m'
unitSI['LineResistance'] = u'Ohm/m'
unitSI['LinFlexibility'] = u'm/N'
unitSI['LinRotRatio'] = u'm/rad'
unitSI['LinStiffness'] = u'N/m'
unitSI['LogarithmicDecrement'] = u'1/S'
unitSI['LogGain'] = u'dB20'
unitSI['LondonPenetrationDepth'] = u'm'
unitSI['LongRangeOrderParameter'] = u'1'
unitSI['LorenzCoefficient'] = u'V2/K2'
unitSI['LossAngle'] = u'rad'
unitSI['Loudness'] = u'sone'
unitSI['LoudnessLevel'] = u'phon'
unitSI['Loundness'] = u'sone'
unitSI['LoundnessLevel'] = u'phon'
unitSI['Luminance'] = u'cd/m2'
unitSI['LuminousEfficacy'] = u'lm/W'
unitSI['LuminousEfficiency'] = u'1'
unitSI['LuminousExitance'] = u'lm/m2'
unitSI['LuminousFlux'] = u'lm'
unitSI['LuminousIntensity'] = u'cd'
unitSI['MachNumber'] = u'1'
unitSI['MacroscopicCrossSection'] = u'm-1'
unitSI['MadelungConstant'] = u'1'
unitSI['MagConductance'] = u'H'
unitSI['MagField'] = u'A/m'
unitSI['MagFieldConstant'] = u'H/m'
unitSI['MagFlux'] = u'Wb'
unitSI['MagFluxDensity'] = u'T'
unitSI['MagFluxDer'] = u'Wb/s'
unitSI['MagneticDipoleMoment'] = u'Wb.m'
unitSI['MagneticFieldStrength'] = u'A/m'
unitSI['MagneticFlux'] = u'Wb'
unitSI['MagneticFluxDensity'] = u'T'
unitSI['MagneticMomentOfParticle'] = u'A.m2'
unitSI['MagneticPolarization'] = u'T'
unitSI['MagneticPotential'] = u'A'
unitSI['MagneticPotentialDifference'] = u'A'
unitSI['MagneticReynoldsNumber'] = u'1'
unitSI['MagneticSusceptibility'] = u'1'
unitSI['MagneticVectorPotential'] = u'Wb/m'
unitSI['Magnetization'] = u'A/m'
unitSI['MagnetomotiveForce'] = u'A'
unitSI['MagPot'] = u'A'
unitSI['MagPotDer'] = u'A/s'
unitSI['MagResistance'] = u'1/H'
unitSI['Mass'] = u'kg'
unitSI['MassAttenuationCoefficient'] = u'm2/kg'
unitSI['MassConcentration'] = u'kg/m3'
unitSI['MassDefect'] = u'kg'
unitSI['MassEnergyTransferCoefficient'] = u'm2/kg'
unitSI['MassExcess'] = u'kg'
unitSI['MassFlow'] = u'kg/s'
unitSI['MassFlowRate'] = u'kg/s'
unitSI['MassFraction'] = u'1'
unitSI['MassieuFunction'] = u'J/K'
unitSI['MassOfElectron'] = u'kg'
unitSI['MassOfMolecule'] = u'kg'
unitSI['MassOfNeutron'] = u'kg'
unitSI['MassOfProton'] = u'kg'
unitSI['MassPerLength'] = u'kg/m'
unitSI['MaximumBetaParticleEnergy'] = u'J'
unitSI['MeanEnergyImparted'] = u'J'
unitSI['MeanFreePath'] = u'm'
unitSI['MeanLife'] = u's'
unitSI['MeanLinearRange'] = u'm'
unitSI['MeanMassRange'] = u'kg/m2'
unitSI['MechanicalImpedance'] = u'N.s/m'
unitSI['MicrocanonicalPartitionFunction'] = u'1'
unitSI['MigrationArea'] = u'm²'
unitSI['MigrationLength'] = u'm'
unitSI['Mobility'] = u'm2/(V.s)'
unitSI['MobilityRatio'] = u'1'
unitSI['ModulusOfAdmittance'] = u'S'
unitSI['ModulusOfElasticity'] = u'Pa'
unitSI['ModulusOfImpedance'] = u'Ohm'
unitSI['MolarAbsorptionCoefficient'] = u'm2/mol'
unitSI['MolarAttenuationCoefficient'] = u'm2/mol'
unitSI['MolarConductivity'] = u'S.m2/mol'
unitSI['MolarDensity'] = u'mol/m3'
unitSI['MolarEnergy'] = u'J/mol'
unitSI['MolarEnthalpy'] = u'J/mol'
unitSI['MolarEntropy'] = u'J/(mol.K)'
unitSI['MolarFlowRate'] = u'mol/s'
unitSI['MolarHeatCapacity'] = u'J/(mol.K)'
unitSI['MolarInternalEnergy'] = u'J/mol'
unitSI['MolarMass'] = u'kg/mol'
unitSI['MolarVolume'] = u'm3/mol'
unitSI['MolecularConcentration'] = u'm-3'
unitSI['MolecularPartitionFunction'] = u'1'
unitSI['MoleFraction'] = u'1'
unitSI['MomentOfForce'] = u'Nm'
unitSI['MomentOfInertia'] = u'kgm²'
unitSI['Momentum'] = u'Ns'
unitSI['MomentumFlux'] = u'N'
unitSI['MomOfArea'] = u'm^4'
unitSI['MutualInductance'] = u'H'
unitSI['NeelTemperature'] = u'K'
unitSI['NeutronFluenceRate'] = u's-1.m-2'
unitSI['NeutronNumber'] = u'1'
unitSI['NeutronNumberDensity'] = u'm-3'
unitSI['NeutronSpeed'] = u'm/s'
unitSI['NeutronYieldPerAbsorption'] = u'1'
unitSI['NeutronYieldPerFission'] = u'1'
unitSI['NonLeakageProbability'] = u'1'
unitSI['NormalStress'] = u'Pa'
unitSI['NuclearMagneton'] = u'A.m2'
unitSI['NuclearPrecessionAngularFrequency'] = u's-1'
unitSI['NuclearQuadrupoleMoment'] = u'm2'
unitSI['NuclearRadius'] = u'm'
unitSI['NucleonNumber'] = u'1'
unitSI['Number'] = u'piece(s)'
unitSI['NumberDensityOfMolecules'] = u'm-3'
unitSI['NumberOfMolecules'] = u'1'
unitSI['NusseltNumber'] = u'1'
unitSI['NusseltNumberOfMassTransfer'] = u'1'
unitSI['OpenLoopGain'] = u'1/s'
unitSI['OrderOfReflexion'] = u'1'
unitSI['OsmoticCoefficientOfSolvent'] = u'1'
unitSI['OsmoticPressure'] = u'Pa'
unitSI['PackingFraction'] = u'1'
unitSI['PartialPressure'] = u'Pa'
unitSI['ParticleDensity'] = u'1/m³'
unitSI['ParticleFluence'] = u'm-2'
unitSI['ParticleFluenceRate'] = u's-1.m2'
unitSI['PathLength'] = u'm'
unitSI['PecletNumber'] = u'1'
unitSI['PecletNumberOfMassTransfer'] = u'1'
unitSI['PeltierCoefficient'] = u'V'
unitSI['Period'] = u's'
unitSI['Permeability'] = u'H/m'
unitSI['PermeabilityOfVacuum'] = u'H/m'
unitSI['Permeance'] = u'H'
unitSI['Permittivity'] = u'F/m'
unitSI['PermittivityOfVacuum'] = u'F/m'
unitSI['PerUnit'] = u'1'
unitSI['PhaseCoefficient'] = u'm-1'
unitSI['PhaseDifference'] = u'rad'
unitSI['PlanckFunction'] = u'J/K'
unitSI['PneuCapacity'] = u'm·s²'
unitSI['PneuInductance'] = u'1/m'
unitSI['PneuResist'] = u'Pa/(kg/s)'
unitSI['PoissonNumber'] = u'1'
unitSI['Position'] = u'm'
unitSI['PotentialDifference'] = u'V'
unitSI['PotentialEnergy'] = u'J'
unitSI['Power'] = u'W'
unitSI['PowerFactor'] = u'1'
unitSI['PowerLevelDifference'] = u'dB'
unitSI['PowerOfSound'] = u'W'
unitSI['PoyntingVector'] = u'W/m2'
unitSI['PrandtlNumber'] = u'1'
unitSI['PressChangePFlowRateChange'] = u'Pa/(m³/s)'
unitSI['Pressure'] = u'Pa'
unitSI['PressureCoefficient'] = u'Pa/K'
unitSI['PressureDifference'] = u'Pa'
unitSI['PropagationCoefficient'] = u'm-1'
unitSI['PropAmplGain'] = u'A/V'
unitSI['ProtonNumber'] = u'1'
unitSI['QuadraticTemperatureCoefficient'] = u'1/K2'
unitSI['QualityFactor'] = u'1'
unitSI['QuantityOfLight'] = u'lm.s'
unitSI['Radiance'] = u'W/(sr.m2)'
unitSI['RadiantEnergy'] = u'J'
unitSI['RadiantEnergyDensity'] = u'J/m3'
unitSI['RadiantEnergyFluenceRate'] = u'W/m2'
unitSI['RadiantExtiance'] = u'W/m2'
unitSI['RadiantIntensity'] = u'W/sr'
unitSI['RadiantPower'] = u'W'
unitSI['Radius'] = u'm'
unitSI['RateOfTempRise'] = u'K/s'
unitSI['RatePressRise'] = u'Pa/s'
unitSI['RatioOfSpecificHeatCapacities'] = u'1'
unitSI['RayleighNumber'] = u'1'
unitSI['Reactance'] = u'Ohm'
unitSI['ReactionEnergy'] = u'J'
unitSI['ReactivePower'] = u'var'
unitSI['Reactivity'] = u'1'
unitSI['ReactorTimeConstant'] = u's'
unitSI['Real'] = u'-'
unitSI['ReciArea'] = u'1/m²'
unitSI['ReciDisplace'] = u'1/m'
unitSI['ReciHeatTransmCoeff'] = u'(m²·K)/W'
unitSI['ReciIntegrAmplGain'] = u'(V/s)/A'
unitSI['ReciPropAmplGain'] = u'V/A'
unitSI['ReciRotVelocity'] = u's/rad'
unitSI['ReciTemp'] = u'1/K'
unitSI['ReciTemp2'] = u'1/°C²'
unitSI['ReciVelocity'] = u's/m'
unitSI['RecombinationCoefficient'] = u'm³/s'
unitSI['ReflectionCoefficient'] = u'1'
unitSI['RefractiveIndex'] = u'1'
unitSI['RelativeAtomicMass'] = u'1'
unitSI['RelativeDensity'] = u'1'
unitSI['RelativeMassDefect'] = u'1'
unitSI['RelativeMassExcess'] = u'1'
unitSI['RelativeMolecularMass'] = u'1'
unitSI['RelativePermeability'] = u'1'
unitSI['RelativePermittivity'] = u'1'
unitSI['RelativePressureCoefficient'] = u'1/K'
unitSI['RelaxationTime'] = u's'
unitSI['RelMagnitude'] = u'-'
unitSI['Reluctance'] = u'H-1'
unitSI['ResidualResistivity'] = u'Ohm·m'
unitSI['Resistance'] = u'Ohm'
unitSI['Resistivity'] = u'Ohm·m'
unitSI['ResonanceEnergy'] = u'J'
unitSI['ResonanceEscapeProbability'] = u'1'
unitSI['ReverberationTime'] = u's'
unitSI['ReynoldsNumber'] = u'1'
unitSI['RichardsonConstant'] = u'A/(m2.K2)'
unitSI['RotAccel'] = u'rad/s²'
unitSI['RotationalDampingConstant'] = u'Nms/rad'
unitSI['RotationalSpringConstant'] = u'Nm/rad'
unitSI['RotDamping'] = u'Nms/rad'
unitSI['RotFlexibility'] = u'rad/Nm'
unitSI['RotLinRatio'] = u'rad/m'
unitSI['RotStiffness'] = u'Nm/rad'
unitSI['RotVelocity'] = u'rad/s'
unitSI['Roughness'] = u'm'
unitSI['SchmidtNumber'] = u'1'
unitSI['SCriticalConduct'] = u'm³/(Pa·s)'
unitSI['SecondMomentOfArea'] = u'm4'
unitSI['SecondPolarMomentOfArea'] = u'm4'
unitSI['SectionModulus'] = u'm3'
unitSI['SeebeckCoefficient'] = u'V/K'
unitSI['SelfInductance'] = u'H'
unitSI['ShearModulus'] = u'Pa'
unitSI['ShearStrain'] = u'1'
unitSI['ShearStress'] = u'Pa'
unitSI['ShortRangeOrderParameter'] = u'1'
unitSI['SlowingDownArea'] = u'm²'
unitSI['SlowingDownDensity'] = u's-1.m-3'
unitSI['SlowingDownLength'] = u'm'
unitSI['SolidAngle'] = u'sr'
unitSI['SoundEnergyDensity'] = u'J/m3'
unitSI['SoundIntensity'] = u'W/m2'
unitSI['SoundParticleAcceleration'] = u'm/s2'
unitSI['SoundParticleDisplacement'] = u'm'
unitSI['SoundParticleVelocity'] = u'm/s'
unitSI['SoundPower'] = u'W'
unitSI['SoundPowerLevel'] = u'dB'
unitSI['SoundPressure'] = u'Pa'
unitSI['SoundPressureLevel'] = u'dB'
unitSI['SoundReductionIndex'] = u'dB'
unitSI['SpecBendDamp'] = u'Nm²s'
unitSI['SpecBendStiff'] = u'Nm²'
unitSI['SpecDamping'] = u'Ns/m²'
unitSI['SpecEnergy'] = u'J/kg'
unitSI['SpecEnthalpy'] = u'J/kg'
unitSI['SpecHeat'] = u'J/(kg·K)'
unitSI['SpecHeatCapacity'] = u'J/(kg·K)'
unitSI['SpecHeatCond'] = u'W/(m·K)'
unitSI['SpecificAcousticImpedance'] = u'Pa.s/m'
unitSI['SpecificActivity'] = u'Bq/kg'
unitSI['SpecificEnergy'] = u'J/kg'
unitSI['SpecificEnergyImparted'] = u'Gy'
unitSI['SpecificEnthalpy'] = u'J/kg'
unitSI['SpecificEntropy'] = u'J/(kg.K)'
unitSI['SpecificGibbsFreeEnergy'] = u'J/kg'
unitSI['SpecificHeatCapacity'] = u'J/(kg.K)'
unitSI['SpecificHeatCapacityAtConstantPressure'] = u'J/(kg.K)'
unitSI['SpecificHeatCapacityAtConstantVolume'] = u'J/(kg.K)'
unitSI['SpecificHeatCapacityAtSaturation'] = u'J/(kg.K)'
unitSI['SpecificHelmholtzFreeEnergy'] = u'J/kg'
unitSI['SpecificInternalEnergy'] = u'J/kg'
unitSI['SpecificVolume'] = u'm3/kg'
unitSI['SpecStiffness'] = u'N/m/m'
unitSI['SpecStretchDamp'] = u'Ns'
unitSI['SpectralAbsorptionFactor'] = u'1'
unitSI['SpectralAngularCrossSection'] = u'm2/(sr.J)'
unitSI['SpectralConcentration'] = u's/m3'
unitSI['SpectralCrossSection'] = u'm2/J'
unitSI['SpectralEmissivity'] = u'1'
unitSI['SpectralLuminousEfficacy'] = u'lm/W'
unitSI['SpectralLuminousEfficiency'] = u'1'
unitSI['SpectralRadianceFactor'] = u'1'
unitSI['SpectralRadiantEnergyDensity'] = u'J/m4'
unitSI['SpectralReflectionFactor'] = u'1'
unitSI['SpectralTransmissionFactor'] = u'1'
unitSI['SpecVolume'] = u'm³/kg'
unitSI['SpecWeight'] = u'N/m³'
unitSI['Speed'] = u'rad/s'
unitSI['StandardAbsoluteActivity'] = u'1'
unitSI['StandardAbsoluteActivityOfSolute'] = u'1'
unitSI['StandardAbsoluteActivityOfSolvent'] = u'1'
unitSI['StantonNumber'] = u'1'
unitSI['StantonNumberOfMassTransfer'] = u'1'
unitSI['StaticPressure'] = u'Pa'
unitSI['StatisticalWeight'] = u'1'
unitSI['StiffnessperArea'] = u'N/m/m²'
unitSI['StoichiometricNumber'] = u'1'
unitSI['Strain'] = u'1'
unitSI['Stress'] = u'Pa'
unitSI['StrouhalNumber'] = u'1'
unitSI['SurfaceCoefficientOfHeatTransfer'] = u'W/(m2.K)'
unitSI['SurfaceDensity'] = u'kg/m2'
unitSI['SurfaceDensityOfCharge'] = u'C/m2'
unitSI['SurfaceTension'] = u'N/m'
unitSI['SurfTens'] = u'N/m'
unitSI['Susceptance'] = u'S'
unitSI['Temp'] = u'K'
unitSI['TempDiff'] = u'K'
unitSI['Temperature'] = u'K'
unitSI['TemperatureDifference'] = u'K'
unitSI['TemperatureSlope'] = u'K/s'
unitSI['TempGrad'] = u'K/s'
unitSI['Temp_C'] = u'degC'
unitSI['Temp_K'] = u'K'
unitSI['Tension'] = u'Pa'
unitSI['ThermalConductance'] = u'W/K'
unitSI['ThermalConductivity'] = u'W/(m.K)'
unitSI['ThermalDiffusionCoefficient'] = u'm2/s'
unitSI['ThermalDiffusionFactor'] = u'1'
unitSI['ThermalDiffusionRatio'] = u'1'
unitSI['ThermalDiffusivity'] = u'm2/s'
unitSI['ThermalInsulance'] = u'm2.K/W'
unitSI['ThermalResistance'] = u'K/W'
unitSI['ThermalUtilizationFactor'] = u'1'
unitSI['ThermConductivity'] = u'W/(m·K)'
unitSI['ThermodynamicTemperature'] = u'K'
unitSI['ThermoelectromotiveForce'] = u'V'
unitSI['Thickness'] = u'm'
unitSI['ThomsonCoefficient'] = u'V/K'
unitSI['Time'] = u's'
unitSI['TimeAging'] = u'1/s'
unitSI['Torque'] = u'Nm'
unitSI['TorqueConst'] = u'Nm/A'
unitSI['TorquePPressChange'] = u'Nm/Pa'
unitSI['TotalAtomicStoppingPower'] = u'J.m2'
unitSI['TotalCrossSection'] = u'm²'
unitSI['TotalIonization'] = u'1'
unitSI['TotalLinearStoppingPower'] = u'J/m'
unitSI['TotalMacroscopicCrossSection'] = u'm-1'
unitSI['TotalMassStoppingPower'] = u'J.m2/kg'
unitSI['TotalNeutronSourceDensity'] = u's-1.m-3'
unitSI['TransCondPar'] = u'A/V²'
unitSI['Transconductance'] = u'A/V2'
unitSI['TranslationalDampingConstant'] = u'N.s/m'
unitSI['TranslationalSpringConstant'] = u'N/m'
unitSI['TransmissionCoefficient'] = u'1'
unitSI['TransportNumberOfIonic'] = u'1'
unitSI['Unbalance'] = u'kgm'
unitSI['Unitless'] = u'-'
unitSI['VAccFeedbackGain'] = u'V/(m/s²)'
unitSI['Velocity'] = u'm/s'
unitSI['VelocityOfSound'] = u'm/s'
unitSI['VeloSound'] = u'm/s'
unitSI['VolExpCoeff'] = u'1/K'
unitSI['VolIncPPressChange'] = u'm³/m/Pa'
unitSI['VolPLength'] = u'm³/m'
unitSI['VolSpecEnergy'] = u'J/m³'
unitSI['Voltage'] = u'V'
unitSI['VoltageSecond'] = u'V.s'
unitSI['VoltageSlope'] = u'V/s'
unitSI['Volume'] = u'm³'
unitSI['VolumeChangePerAngleChange'] = u'm³/rad'
unitSI['VolumeDensityOfCharge'] = u'C/m3'
unitSI['VolumeFlow'] = u'm³/s'
unitSI['VolumeFlowRate'] = u'm³/s'
unitSI['VolumeFraction'] = u'1'
unitSI['VolumeStrain'] = u'1'
unitSI['VPosFeedbackGain'] = u'V/m'
unitSI['VPressFeedbackGain'] = u'V/Pa'
unitSI['VROCPressFeedbackGain'] = u'V/(Pa/s)'
unitSI['VRotAccFeedbackGain'] = u'V/(rad/s²)'
unitSI['VRotAngleFeedbackGain'] = u'V/rad'
unitSI['VRotVeloFeedbackGain'] = u'V/(rad/s)'
unitSI['VVeloFeedbackGain'] = u'V/(m/s)'
unitSI['Wavelength'] = u'm'
unitSI['WaveNumber'] = u'm-1'
unitSI['WeberNumber'] = u'1'
unitSI['Weight'] = u'N'
unitSI['Work'] = u'J'
