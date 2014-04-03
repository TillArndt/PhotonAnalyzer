import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_100_1_Psf.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_101_1_TVJ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_102_4_mVK.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_103_1_xB2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_104_1_da5.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_105_1_uwA.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_106_4_HoH.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_107_1_SrS.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_108_1_ry2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_109_1_kkA.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_10_2_ahu.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_110_1_fWB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_111_1_WwS.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_112_1_cxB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_113_1_Tgs.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_114_1_BU2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_115_1_OMq.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_116_1_MAR.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_117_1_Wkj.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_118_1_wlf.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_119_1_jU8.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_11_1_X6m.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_120_1_Xlp.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_121_1_W8y.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_122_1_pCc.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_123_1_Ip7.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_124_1_REI.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_125_4_qGK.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_126_2_A0h.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_127_5_7e7.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_128_1_E1b.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_129_1_hGF.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_12_1_0om.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_130_1_4tx.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_131_1_LuO.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_132_1_DyJ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_133_1_eqW.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_134_1_19K.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_135_4_1xV.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_136_1_r0O.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_137_1_Tdu.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_138_1_AQn.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_139_1_biU.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_13_1_aq0.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_140_1_uTZ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_141_5_mFe.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_142_1_92X.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_143_1_fYB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_144_1_zy1.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_145_1_ejS.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_146_1_Zxn.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_147_1_aiX.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_148_1_264.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_149_1_Y1C.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_14_1_0ew.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_150_1_5UZ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_151_1_h0u.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_152_1_SqN.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_153_3_neC.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_154_1_shf.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_155_1_wfF.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_156_1_yRX.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_157_1_cKl.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_158_1_vIK.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_159_1_yuD.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_15_1_4OB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_160_1_fP0.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_160_1_yrk.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_161_1_DDA.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_162_1_kAU.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_163_1_yFw.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_164_1_l1M.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_165_1_JSB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_166_3_6PZ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_167_1_cTA.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_168_1_2jC.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_169_1_GGm.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_16_1_mhP.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_170_1_NxH.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_171_1_2ki.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_172_1_VnY.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_173_1_LU6.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_174_1_Con.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_175_1_q40.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_176_1_H6E.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_177_1_LEt.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_178_1_j89.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_179_1_erA.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_17_1_Efi.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_180_1_Gek.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_181_1_zjN.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_182_1_w6p.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_183_1_OCF.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_184_1_JoS.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_185_1_ear.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_186_1_2ny.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_187_1_Zz9.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_188_1_mNE.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_189_1_66Z.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_18_1_s7E.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_190_1_1C6.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_191_1_rF4.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_192_1_s1x.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_193_1_vpz.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_194_1_j94.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_195_1_xvC.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_196_1_5XL.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_197_1_hBp.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_198_1_MDB.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_199_1_ADJ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_19_1_Npc.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_1_1_euY.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_200_1_srg.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_201_1_oZZ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_20_1_hSV.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_21_1_VwY.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_22_1_nP9.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_23_1_iWZ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_24_1_cnW.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_25_1_zNM.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_26_1_2s0.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_27_1_Da4.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_28_1_L8y.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_29_1_xpj.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_2_1_Yqt.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_30_1_A5V.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_30_1_vet.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_31_1_7Ku.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_32_1_Wc7.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_33_4_3GO.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_34_1_dtd.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_35_1_n8Q.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_36_1_OEp.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_37_1_qSq.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_38_1_kmz.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_39_1_YGS.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_3_1_Etu.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_40_1_IQi.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_41_1_xsK.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_42_1_OL5.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_43_4_QQe.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_44_1_ExR.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_45_1_ftr.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_46_1_ztN.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_47_4_GAI.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_48_1_Q3b.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_49_1_ep9.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_4_1_5uH.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_50_1_Exz.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_51_1_JAa.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_52_1_IKI.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_53_1_byG.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_54_4_aaM.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_55_2_5AQ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_56_1_o72.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_57_1_AY2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_58_1_kS2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_59_1_9qu.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_5_1_7G5.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_60_1_shY.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_61_1_LgT.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_62_1_e4w.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_63_1_Bhc.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_64_1_XEz.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_65_1_kzK.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_66_1_t71.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_67_1_oB3.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_68_1_LCe.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_69_1_TSX.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_6_1_WY2.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_70_1_C1F.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_71_1_sMv.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_72_2_WwR.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_73_4_XZT.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_74_1_mr7.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_75_1_ISJ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_76_1_zZD.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_77_1_hq5.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_78_1_4f8.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_79_1_xZr.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_80_1_iLU.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_81_1_gZG.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_82_1_Kyu.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_83_1_3qs.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_84_1_X79.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_85_1_pyN.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_86_1_JVV.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_87_1_Gto.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_88_1_ueE.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_89_1_Lsg.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_8_1_iDH.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_90_1_jET.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_91_1_nDk.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_92_1_Tv5.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_93_1_wTt.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_94_1_V4O.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_95_1_Dsn.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_96_1_QkQ.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_97_1_vRm.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_98_1_e21.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_99_1_dGb.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_99_1_ePj.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_9_1_Ih4.root',
'file:/net/scratch_cms/institut_3b/arndt/GluGluToHToGG_M-125_13TeV-powheg-pythia6/GluGluToHToGG_M-125_13TeV-powheg-pythia6_EGM700_PU40bx25_POSTLS170_V4-v1_9_1_KUt.root',


	)
)

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('Output_PU40.root')
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
