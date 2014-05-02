// -*- C++ -*-
//
// Package:    PhotonAnalyzer/PhotonAnalyzer
// Class:      PhotonAnalyzer
// 
/**\class PhotonAnalyzer PhotonAnalyzer.cc PhotonAnalyzer/PhotonAnalyzer/plugins/PhotonAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Till Arndt
//         Created:  Mon, 17 Feb 2014 10:25:23 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TGraphAsymmErrors.h"
#include "TLorentzVector.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
//
// class declaration
//

class PhotonAnalyzer : public edm::EDAnalyzer {
   public:
      explicit PhotonAnalyzer(const edm::ParameterSet&);
      ~PhotonAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
     TH1D *hist_photon_pt;
     TH1D *hist_matchphoton_pt;
     TGraphAsymmErrors *graph_purity_pt;
     
     TH1D *hist_photon_eta;
     TH1D *hist_matchphoton_eta;
     TGraphAsymmErrors *graph_purity_eta;
         
     TH1D *hist_genphoton_nvtx;
     TH1D *hist_matchgenphoton_nvtx;
     TGraphAsymmErrors *graph_efficiency_nvtx;	
      
     TH1D *hist_genphoton_pt;
     TH1D *hist_matchgenphoton_pt;
     TGraphAsymmErrors *graph_efficiency_pt;

     TH1D *hist_genphoton_eta;
     TH1D *hist_matchgenphoton_eta;
     TGraphAsymmErrors *graph_efficiency_eta;
     TH1D *hist_rebin_genphoton_pt;
     TH1D *hist_rebin_matchgenphoton_pt; 


     //ID Stuff
     
     TH1D *hist_matchphoton_nvtx; 
     TH1D *hist_matchphoton_loose_nvtx;
     TH1D *hist_matchphoton_medium_nvtx;
     TH1D *hist_matchphoton_tight_nvtx;

     TH1D *hist_matchphoton_loose_pt;
     TH1D *hist_matchphoton_medium_pt;
     TH1D *hist_matchphoton_tight_pt;
  
     TH1D *hist_matchphoton_loose_eta;
     TH1D *hist_matchphoton_medium_eta;
     TH1D *hist_matchphoton_tight_eta;

     TGraphAsymmErrors *graph_id_efficiency_nvtx_loose;
     TGraphAsymmErrors *graph_id_efficiency_nvtx_medium;
     TGraphAsymmErrors *graph_id_efficiency_nvtx_tight;

     TGraphAsymmErrors *graph_id_efficiency_pt_loose;
     TGraphAsymmErrors *graph_id_efficiency_pt_medium;
     TGraphAsymmErrors *graph_id_efficiency_pt_tight;

     TGraphAsymmErrors *graph_id_efficiency_eta_loose;
     TGraphAsymmErrors *graph_id_efficiency_eta_medium;
     TGraphAsymmErrors *graph_id_efficiency_eta_tight;



     TH1D *hist_rebin_photon_pt;
     TH1D *hist_rebin_matchphoton_pt;
     double_t rebin_array[34]= {0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95.,100.,105.,110.,115.,120.,125.,130.,135.,140.,145.,150.,200.,300.,500.};

     TLorentzVector vec_genphoton;
     TLorentzVector vec_photon;
     int allphotons;
     int matchedphotons;
     int allgenphotons;
     int matchedgenphotons;
     bool barrel;
     bool isLoose;
     bool isMedium;
     bool isTight;
    
     double nVtx;
     virtual bool findHiggs(const reco::Candidate*);
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PhotonAnalyzer::PhotonAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

 barrel = iConfig.getParameter<bool>("barrel");

 edm::Service<TFileService> fs;
 hist_photon_pt = fs->make<TH1D>("hist_photon_pt" , "Photon_Pt" , 100 , 0 , 500 );
 hist_matchphoton_pt = fs->make<TH1D>("hist_matchphoton_pt","Match_Photon_Pt",100,0,500);
 hist_photon_pt->Sumw2();
 hist_matchphoton_pt->Sumw2();


hist_rebin_photon_pt = fs->make<TH1D>("hist_rebin_photon_pt" , "Photon_Pt"  , 33,rebin_array);
hist_rebin_matchphoton_pt = fs->make<TH1D>("hist_rebin_matchphoton_pt","Match_Photon_Pt",33,rebin_array);

 hist_photon_eta = fs->make<TH1D>("hist_photon_eta" , "Photon_eta" , 51 , -5 , 5 );
 hist_matchphoton_eta = fs->make<TH1D>("hist_matchphoton_eta","Matched_Photon_eta",51,-5,5);
 hist_photon_eta->Sumw2();
 hist_matchphoton_eta->Sumw2();

 graph_purity_pt = fs->make<TGraphAsymmErrors>();
 graph_purity_eta = fs->make<TGraphAsymmErrors>();

 graph_purity_pt->SetName("graph_purity_pt");
 graph_purity_eta->SetName("graph_purity_eta");
 
 hist_genphoton_pt = fs->make<TH1D>("hist_genphoton_pt" , "Gen_Photon_Pt" , 100 , 0 , 500 );
 hist_matchgenphoton_pt = fs->make<TH1D>("hist_matchgenphoton_pt","Match_Gen_Photon_Pt",100,0,500);
 hist_genphoton_pt->Sumw2();
 hist_matchgenphoton_pt->Sumw2();

 hist_genphoton_eta = fs->make<TH1D>("hist_genphoton_eta" , "Gen_Photon_eta" , 51 , -5 , 5 );
 hist_matchgenphoton_eta = fs->make<TH1D>("hist_matchgenphoton_eta","Matched_Gen_Photon_eta",51,-5,5);
 hist_genphoton_eta->Sumw2();
 hist_matchgenphoton_eta->Sumw2();

 hist_genphoton_nvtx = fs->make<TH1D>("hist_genphoton_nvtx" , "Gen_Photon_nvtx" , 50 , 0 , 50 );
 hist_matchgenphoton_nvtx = fs->make<TH1D>("hist_matchgenphoton_nvtx","Matched_Gen_Photon_nvtx",50,0,50);
 hist_genphoton_nvtx->Sumw2();
 hist_matchgenphoton_nvtx->Sumw2();

 graph_efficiency_pt = fs->make<TGraphAsymmErrors>();
 graph_efficiency_eta = fs->make<TGraphAsymmErrors>();
 graph_efficiency_nvtx = fs->make<TGraphAsymmErrors>();

 graph_efficiency_pt->SetName("graph_effiency_pt");
 graph_efficiency_eta->SetName("graph_efficiency_eta");
 graph_efficiency_nvtx->SetName("graph_efficiency_nvtx");

//ID Stuff

 hist_matchphoton_nvtx = fs->make<TH1D>("hist_matchphoton_nvtx" , "# Vertices" , 50 , 0 , 50 );
 hist_matchphoton_loose_nvtx = fs->make<TH1D>("hist_matchphoton_loose_nvtx","# Vertices Loose",50,0,50);
 hist_matchphoton_medium_nvtx = fs->make<TH1D>("hist_matchphoton_medium_nvtx" , "# Vertices Medium" , 50 , 0 , 50 );
 hist_matchphoton_tight_nvtx = fs->make<TH1D>("hist_matchphoton_tight_nvtx","# Vertices Tight",50,0,50);
 hist_matchphoton_nvtx->Sumw2();
 hist_matchphoton_loose_nvtx->Sumw2();
 hist_matchphoton_medium_nvtx->Sumw2();
 hist_matchphoton_tight_nvtx->Sumw2();

 hist_matchphoton_loose_pt = fs->make<TH1D>("hist_matchphoton_loose_pt","Photon_Pt Loose",33,rebin_array);
 hist_matchphoton_medium_pt = fs->make<TH1D>("hist_matchphoton_medium_pt" , "Photon_Pt Medium" , 33, rebin_array );
 hist_matchphoton_tight_pt = fs->make<TH1D>("hist_matchphoton_tight_pt","Photon_Pt Tight",33, rebin_array);
 hist_matchphoton_loose_pt->Sumw2();
 hist_matchphoton_medium_pt->Sumw2();
 hist_matchphoton_tight_pt->Sumw2();

 hist_matchphoton_loose_eta = fs->make<TH1D>("hist_matchphoton_loose_eta","Photon_#eta Loose",51,-5,5);
 hist_matchphoton_medium_eta = fs->make<TH1D>("hist_matchphoton_medium_eta" , "Photon_#eta Medium" , 51,-5,5 );
 hist_matchphoton_tight_eta = fs->make<TH1D>("hist_matchphoton_tight_eta","Photon_#eta Tight",51,-5,5);
 hist_matchphoton_loose_eta->Sumw2();
 hist_matchphoton_medium_eta->Sumw2();
 hist_matchphoton_tight_eta->Sumw2();

 graph_id_efficiency_nvtx_loose = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_nvtx_medium = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_nvtx_tight = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_nvtx_loose->SetName("graph_id_effiency_nvtx_loose");
 graph_id_efficiency_nvtx_medium->SetName("graph_id_efficiency_nvtx_medium");
 graph_id_efficiency_nvtx_tight->SetName("graph_id_efficiency_nvtx_tight");

 graph_id_efficiency_pt_loose = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_pt_medium = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_pt_tight = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_pt_loose->SetName("graph_id_effiency_pt_loose");
 graph_id_efficiency_pt_medium->SetName("graph_id_efficiency_pt_medium");
 graph_id_efficiency_pt_tight->SetName("graph_id_efficiency_pt_tight");

 graph_id_efficiency_eta_loose = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_eta_medium = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_eta_tight = fs->make<TGraphAsymmErrors>();
 graph_id_efficiency_eta_loose->SetName("graph_id_effiency_eta_loose");
 graph_id_efficiency_eta_medium->SetName("graph_id_efficiency_eta_medium");
 graph_id_efficiency_eta_tight->SetName("graph_id_efficiency_eta_tight");



 
 vec_photon = TLorentzVector();
 vec_genphoton= TLorentzVector();
 
 allphotons = 0;
 matchedphotons =0;
 allgenphotons = 0;
 matchedgenphotons = 0;

 isLoose = false;
 isMedium = false;
 isTight = false;
 
}


PhotonAnalyzer::~PhotonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//


bool PhotonAnalyzer::findHiggs(const reco::Candidate* part){
	if (part->pdgId() == 25) return true;
	else if (part->numberOfMothers() == 0) return false;
	else return findHiggs(part->mother(0));

}

// ------------ method called for each event  ------------
void
PhotonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;
   using namespace reco;  

 
//vector<reco::GenParticle>             "genParticles"              ""                "SIM"     




	
   edm::Handle<edm::View<reco::Photon>> photons;
   edm::Handle<edm::View<reco::GenParticle>> genphotons;
   edm::Handle<double> rho_corr;
   
  // size_t nMaps =matchMaps_.size();
  // std::vector<const GenParticleMatch *> maps;
   Handle<Association<reco::GenParticleCollection>> mcMatchMap;
   Handle<Association<reco::GenParticleCollection>> mcGenMatchMap;	
   iEvent.getByLabel("PhotonProducer",mcMatchMap);
   iEvent.getByLabel("GenPhotonProducer",mcGenMatchMap);
   
   iEvent.getByLabel("gedPhotons",photons);
   iEvent.getByLabel("genParticles",genphotons);
   iEvent.getByLabel("fixedGridRhoFastjetAll",rho_corr);

   edm::Handle<reco::BeamSpot> bsHandle; 
   iEvent.getByLabel("offlineBeamSpot", bsHandle);
   const reco::BeamSpot &beamspot = *bsHandle.product();

   edm::Handle<reco::ConversionCollection> hConversions;
   iEvent.getByLabel("allConversions", hConversions);

   edm::Handle<reco::GsfElectronCollection> hElectrons;
   iEvent.getByLabel("gedGsfElectrons", hElectrons);

   edm::Handle<edm::View<reco::Vertex>> vertices;
   iEvent.getByLabel("offlinePrimaryVertices", vertices);

 
   nVtx = vertices->size();

for(edm::View<reco::GenParticle>::const_iterator genphoton = genphotons->begin();genphoton!=genphotons->end(); genphoton++){ 
 		
	if (genphoton->pdgId() ==22 && genphoton->status()==1){
		if(genphoton->pt()<=15.) continue;
		if(barrel && std::abs(genphoton->eta())> 1.479) continue;
		if (!barrel && (std::abs(genphoton->eta())< 1.5 || std::abs(genphoton->eta())>3.) ) continue;
                hist_genphoton_pt->Fill(genphoton->pt());
                hist_genphoton_eta->Fill(genphoton->eta());
                hist_genphoton_nvtx->Fill(nVtx);
		allgenphotons++;
	}

}  

  
 //  std::cout<<"Photons "<<photons->size()<<std::endl;
   for (unsigned int i =0; i<photons->size();i++){
    //            std::cout<<" i "<<i;
//	        std::cout<< " test pt "<<(*photons)[i].pt() <<std::endl;
        if((*photons)[i].pt()<15.) continue;
        if(barrel && std::abs((*photons)[i].eta())> 1.479) continue;
        if (!barrel && (std::abs((*photons)[i].eta())< 1.5 || std::abs((*photons)[i].eta())>3.) ) continue; 
        bool passelectronveto = !ConversionTools::hasMatchedPromptElectron((*photons)[i].superCluster(), hElectrons, hConversions, beamspot.position());
	bool SingleTower = ((*photons)[i].hadTowOverEm() < 0.05);
        double sigmaIetaIeta = (*photons)[i].sigmaIetaIeta();
	double eA_charged = 0;
	double eA_neutral= 0;
	double eA_photons= 0;
	if (std::abs((*photons)[i].eta())< 1.0) eA_charged = 0.012, eA_neutral = 0.030, eA_photons = 0.148 ;
	else if (std::abs((*photons)[i].eta())> 1.0 && std::abs((*photons)[i].eta())< 1.479 ) eA_charged = 0.010, eA_neutral = 0.057, eA_photons = 0.130 ;
	else if (std::abs((*photons)[i].eta())> 1.479 && std::abs((*photons)[i].eta())< 2.0 ) eA_charged = 0.014, eA_neutral = 0.039, eA_photons = 0.112 ;
	else if (std::abs((*photons)[i].eta())> 2.0 && std::abs((*photons)[i].eta())< 2.2 ) eA_charged = 0.012, eA_neutral = 0.015, eA_photons = 0.216 ;
	else if (std::abs((*photons)[i].eta())> 2.2 && std::abs((*photons)[i].eta())< 2.3 ) eA_charged = 0.016, eA_neutral = 0.024, eA_photons = 0.262 ;
	else if (std::abs((*photons)[i].eta())> 2.3 && std::abs((*photons)[i].eta())< 2.4 ) eA_charged = 0.020, eA_neutral = 0.039, eA_photons = 0.260 ;
	else if (std::abs((*photons)[i].eta())> 2.4 ) eA_charged = 0.012, eA_neutral = 0.072, eA_photons = 0.266 ; 
	double chargedIso = std::max((*photons)[i].chargedHadronIso() - ((*rho_corr) * eA_charged),0.);
	double neutralIso = std::max((*photons)[i].neutralHadronIso() - ((*rho_corr) * eA_neutral),0.);
	double photonIso = std::max((*photons)[i].photonIso() - ((*rho_corr) * eA_photons),0.);
        
       	//std::cout<<"charged Iso: "<< chargedIso<<std::endl;
	//std::cout<<"neutral Iso: "<< neutralIso<<std::endl;
	//std::cout<<"photon Iso: "<< photonIso<<std::endl;
	//std::cout<<"sigmaIetaIeta : "<< sigmaIetaIeta<<std::endl;

 
        isLoose = false;
	isMedium = false;
	isTight = false;        
 
	if (barrel && passelectronveto && SingleTower && sigmaIetaIeta < 0.012 && chargedIso < 2.6 && neutralIso < (3.5 + 0.04 * (*photons)[i].pt()) && photonIso < (1.3 + (0.005 * (*photons)[i].pt()))){
		isLoose = true;
	//	std::cout<<"isLoose"<<std::endl;
		if(sigmaIetaIeta < 0.011 && chargedIso < 1.5 && neutralIso < (1.0 + (0.04 * (*photons)[i].pt())) && photonIso < (0.7 + (0.005 * (*photons)[i].pt()))){
			isMedium = true;
	//		std::cout<<"isMedium"<<std::endl;
			if (chargedIso < 0.7 && neutralIso < (0.4 + (0.04 * (*photons)[i].pt())) && photonIso < (0.5 + (0.005 * (*photons)[i].pt()))){
				isTight = true;
	//			std::cout<<"isTight"<<endl;
			}
		}
	}

        if (!barrel && passelectronveto && SingleTower && sigmaIetaIeta < 0.034 && chargedIso < 2.3 && neutralIso < (2.9 + 0.04 * (*photons)[i].pt())){
                isLoose = true;
                if(sigmaIetaIeta < 0.033 && chargedIso < 1.2 && neutralIso < (1.5+ (0.04 * (*photons)[i].pt())) && photonIso < (1.0 + (0.005 * (*photons)[i].pt()))){
                        isMedium = true;
                        if (sigmaIetaIeta < 0.031 && chargedIso < 0.5 && neutralIso < (1.5 + (0.04 * (*photons)[i].pt())) && photonIso < (1. + (0.005 * (*photons)[i].pt()))){
                        isTight = true;
	//		std::cout<<"isTight"<<endl;

                        }
                }
        }

        hist_photon_pt->Fill((*photons)[i].pt());
	hist_photon_eta->Fill((*photons)[i].eta());
        allphotons ++;
	RefToBase<reco::Photon> photonref = photons->refAt(i);
	reco::Photon photon(*(photonref.get()));
	reco::GenParticleRef matchref = (*mcMatchMap)[photonref];
	if (matchref.isNonnull() && matchref.isAvailable() && findHiggs(matchref.get()->mother(0))){
	        //std::cout<<"last mother: " << matchref.get()->mother(matchref.get()->numberOfMothers()-1)->pdgId() <<endl;
	        //std::cout<<"first mother: " << matchref.get()->mother(0)->pdgId() <<endl;
		//std::cout<<"number of mothers :"<<matchref.get()->numberOfMothers()<<endl;

		hist_matchphoton_pt->Fill(photon.pt());
		hist_matchphoton_eta->Fill(photon.eta());
		hist_matchphoton_nvtx->Fill(nVtx);
		if (isLoose){ hist_matchphoton_loose_nvtx->Fill(nVtx);
			 hist_matchphoton_loose_pt->Fill(photon.pt());
			hist_matchphoton_loose_eta->Fill(photon.eta());}
		if (isMedium){ hist_matchphoton_medium_nvtx->Fill(nVtx);
				 hist_matchphoton_medium_pt->Fill(photon.pt());
				 hist_matchphoton_medium_eta->Fill(photon.eta());}
		if (isTight){ hist_matchphoton_tight_nvtx->Fill(nVtx);
				hist_matchphoton_tight_pt->Fill(photon.pt());
				hist_matchphoton_tight_eta->Fill(photon.eta());
	//			std::cout<<"isTight"<<endl;

			    }				  
		
		matchedphotons++;
	}
	}

   for (unsigned int i =0; i<photons->size();i++){
    //            std::cout<<" i "<<i;
//              std::cout<< " test pt "<<(*photons)[i].pt() <<std::endl;
        if((*photons)[i].pt()<=15.) continue;
        if(barrel && std::abs((*photons)[i].eta())> 1.479) continue;
        if (!barrel && (std::abs((*photons)[i].eta())< 1.5 || std::abs((*photons)[i].eta()>3.)) ) continue;

        RefToBase<reco::Photon> photonref = photons->refAt(i);
        reco::Photon photon(*(photonref.get()));
        reco::GenParticleRef matchref = (*mcGenMatchMap)[photonref];
        if (matchref.isNonnull() && matchref.isAvailable()){
	        if(matchref.get()->pt()<=15.) continue;
                if(barrel && std::abs(matchref.get()->eta())> 1.479) continue;
	        if (!barrel && (std::abs(matchref.get()->eta())< 1.5 || std::abs(matchref.get()->eta())>3.) ) continue;
		hist_matchgenphoton_pt->Fill(matchref.get()->pt());
                hist_matchgenphoton_eta->Fill(matchref.get()->eta());
		hist_matchgenphoton_nvtx->Fill(nVtx);
                matchedgenphotons ++;
        }



	}
  /* for(edm::View<reco::Photon>::const_iterator photon = photons->begin();photon!=photons->end(); ++photon){	
	//std::cout<< "test pt "<<photon->pt() <<std::endl;
	hist_photon_pt->Fill(photon->pt());
	vec_photon.SetPtEtaPhiE(photon->pt(),photon->eta(),photon->phi(),photon->p4().e());
	for(edm::View<reco::GenParticle>::const_iterator genphoton = genphotons->begin();genphoton!=genphotons->end(); genphoton++){ 
		vec_genphoton.SetPtEtaPhiE(genphoton->pt(),genphoton->eta(),genphoton->phi(),genphoton->p4().e());
		if (genphoton->pdgId() ==22 && vec_genphoton.DeltaR(vec_photon)<0.2){ 
			hist_genphoton_pt->Fill(genphoton->pt());
			break;			
		}
	}
   }*/
}


// ------------ method called once each job just before starting event loop  ------------
void 
PhotonAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PhotonAnalyzer::endJob(){ 

hist_rebin_photon_pt = (TH1D*) hist_photon_pt->Rebin(33,"hist_rebin_photon_pt",rebin_array);
hist_rebin_matchphoton_pt = (TH1D*) hist_matchphoton_pt->Rebin(33,"hist_rebin_matchphoton_pt",rebin_array);

graph_purity_pt->Divide(hist_rebin_matchphoton_pt,hist_rebin_photon_pt);
graph_purity_eta->Divide(hist_matchphoton_eta,hist_photon_eta);

hist_rebin_genphoton_pt = (TH1D*) hist_genphoton_pt->Rebin(33,"hist_rebin_genphoton_pt",rebin_array);
hist_rebin_matchgenphoton_pt = (TH1D*) hist_matchgenphoton_pt->Rebin(33,"hist_rebin_matchgenphoton_pt",rebin_array);


graph_efficiency_pt->Divide(hist_rebin_matchgenphoton_pt,hist_rebin_genphoton_pt);
graph_efficiency_eta->Divide(hist_matchgenphoton_eta,hist_genphoton_eta);
graph_efficiency_nvtx->Divide(hist_matchgenphoton_nvtx,hist_genphoton_nvtx);

graph_id_efficiency_nvtx_loose->Divide(hist_matchphoton_loose_nvtx,hist_matchphoton_nvtx);
graph_id_efficiency_nvtx_medium->Divide(hist_matchphoton_medium_nvtx,hist_matchphoton_nvtx);
graph_id_efficiency_nvtx_tight->Divide(hist_matchphoton_tight_nvtx,hist_matchphoton_nvtx);

graph_id_efficiency_pt_loose->Divide(hist_matchphoton_loose_pt,hist_rebin_matchphoton_pt);
graph_id_efficiency_pt_medium->Divide(hist_matchphoton_medium_pt,hist_rebin_matchphoton_pt);
graph_id_efficiency_pt_tight->Divide(hist_matchphoton_tight_pt,hist_rebin_matchphoton_pt);

graph_id_efficiency_eta_loose->Divide(hist_matchphoton_loose_eta,hist_matchphoton_eta);
graph_id_efficiency_eta_medium->Divide(hist_matchphoton_medium_eta,hist_matchphoton_eta);
graph_id_efficiency_eta_tight->Divide(hist_matchphoton_tight_eta,hist_matchphoton_eta);



std::cout<<"Efficiency = " << matchedphotons<<"/"<<allphotons <<" Signal Efficiency = "<<matchedgenphotons<<"/"<<allgenphotons << std::endl;
}

// ------------ method called when starting to processes a run  ------------
/*
void 
PhotonAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
PhotonAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
PhotonAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
PhotonAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PhotonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PhotonAnalyzer);
