import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/user/arndt/Files/EGamma/Htogg13_PU50/1E896AAA-F68F-E311-8C49-00261894390A.root',
	'file:/user/arndt/Files/EGamma/Htogg13_PU50/8AC0DE66-0490-E311-90B1-0025905A60B2.root',
	'file:/user/arndt/Files/EGamma/Htogg13_PU50/E8DAF5CE-3490-E311-A8D3-001A92810AB2.root',
	'file:/user/arndt/Files/EGamma/Htogg13_PU50/8A9786EA-F28F-E311-945B-003048FFD752.root',
	'file:/user/arndt/Files/EGamma/Htogg13_PU50/E83C645D-F48F-E311-A6A3-0025905A605E.root',
	'file:/user/arndt/Files/EGamma/Htogg13_PU50/F6FCDF33-F28F-E311-A893-002618943985.root'
	)
)

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('Output_PU50.root')
                                   )

process.PhotonProducer = cms.EDProducer("MCMatcher", # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src = cms.InputTag("gedPhotons"), # RECO objects to match
    matched = cms.InputTag("genParticles"), # mc-truth particle collection
    mcPdgId = cms.vint32(22), # one or more PDG ID (11 = electron); absolute values (see below)
    checkCharge = cms.bool(True), # True = require RECO and MC objects to have the same charge
    mcStatus = cms.vint32(1), # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR = cms.double(0.2), # Minimum deltaR for the match
    maxDPtRel = cms.double(.3), # Minimum deltaPt/Pt for the match
    resolveAmbiguities = cms.bool(True), # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True), # False = just match input in order; True = pick lowest deltaR pair first
)

process.GenPhotonProducer = cms.EDProducer("MCMatcher", # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src = cms.InputTag("gedPhotons"), # RECO objects to match
    matched = cms.InputTag("genParticles"), # mc-truth particle collection
    mcPdgId = cms.vint32(22), # one or more PDG ID (11 = electron); absolute values (see below)
    checkCharge = cms.bool(True), # True = require RECO and MC objects to have the same charge
    mcStatus = cms.vint32(1), # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR = cms.double(0.2), # Minimum deltaR for the match
    maxDPtRel = cms.double(.3), # Minimum deltaPt/Pt for the match
    resolveAmbiguities = cms.bool(True), # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True), # False = just match input in order; True = pick lowest deltaR pair first
)


process.PhotonAnalyzer_Barrel = cms.EDAnalyzer('PhotonAnalyzer',
   barrel = cms.bool(True),
)

process.PhotonAnalyzer_Endcap = cms.EDAnalyzer('PhotonAnalyzer',
   barrel = cms.bool(False),
)




#process.sequence = cms.Sequence(process.PhotonProducer * process.PhotonAnalyzer)
process.p = cms.Path(process.PhotonProducer * process.GenPhotonProducer * process.PhotonAnalyzer_Barrel * process.PhotonAnalyzer_Endcap)
