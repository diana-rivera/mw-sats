import numpy as np
import pandas as pd


gal=['Draco','Carina','Ursa Minor','Leo I','Leo II','Sextans','Fornax','Sculptor'] #classical satellite galaxies
num=[393,717,309,464,192,385,5603,2360] #number of stars in the galaxy data
mass=[0.022,0.00151,'NAN',0.02,0.027,0.3,0.054,'NAN'] #billion solar masses
c_ra_e = [(1.8500238333333527,-1.159572166666635),(0.9540833333333438,-0.8854606666666456),(1.6546310000000233,-1.0649819999999863),(0.22913533333334613,-0.22206666666664887),(0.1490146666666874,-0.18916233333331434),(0.7542456666666908,-0.74033533333332),(0.6512696666666713,-0.7077683333333269),(0.927560333333334,-1.1646486666666647)]
c_dec_e = [(0.5776055555555573,-0.4630864444444427),(0.5207211111111008,-0.578050888888896),(0.5522138888888861,-0.7720181111111089),(0.11233699999999835,-0.11529200000000195),(0.0951034444444474,-0.09851555555555436),(0.7472532222222223,-0.6775167777777775),(0.4850046666666614,-0.7796623333333343),(0.4837008888888832,-0.4160221111111113)]
Mv_error = pd.DataFrame({'Mv_error': [(-0.05,0.05),(-0.05,0.05),(-0.05,0.05),(-0.28,0.28),(-0.04,0.04),(-0.06,0.06),(-0.14,0.14),(-0.14,0.14)]})
r1_2_error = pd.DataFrame({'r1_2_error': [(-17,17),(-15,15),(-21,21),(-16,17),(-10,10),(-15,15),(-18,18),(-16,16)]})
dist_error = pd.DataFrame({'dist_error': [(-6.0,6.0),(-5.0,5.0),(-4.0,4.0),(-15.0,16.0),(-14.0,14.0),(-3.0,3.0),(-3.0,3.0),(-5.0,5.0)]})
Vhel_error = pd.DataFrame({'Vhel_error': [(-0.8,0.7),(-0.1,0.1),(-0.8,0.8),(-0.5,0.5),(-0.6,0.6),(-0.1,0.1),(-0.1,0.1),(-0.1,0.1)]})
sigma_error = pd.DataFrame({'sigma_error': [(-1.2,1.2),(-1.2,1.2),(-1.2,1.2),(-0.4,0.4),(-0.4,0.4),(-1.3,1.3),(-0.9,0.9),(-1.1,1.1)]})
Fe_H_error = pd.DataFrame({'Fe_H_error': [(-0.02,0.02),(-0.02,0.02),(-0.02,0.03),(-0.01,0.02),(-0.03,0.02),(-0.04,0.04),(-0.01,0.02),(-0.02,0.03)]})
sigFe_H_error = pd.DataFrame({'sigFe_H_error': [(-0.02,0.02),'NAN',(-0.03,0.02),(-0.01,0.01),(-0.02,0.02),(-0.03,0.03),(-0.01,0.01),(-0.02,0.02)]})


a=pd.read_csv('coor.csv')
b=pd.read_csv('dist.csv')
c=pd.read_csv('err_ra.csv')
e=pd.read_csv('err_dec.csv')
h=pd.read_csv("new_b.csv")



import sat_array
from importlib import reload
reload(sat_array)

d = np.zeros(1, dtype=sat_array.mydtype).view(np.recarray)

d['gal']=gal


draco = pd.read_csv('draco_filtered.csv')
draco_mw = pd.read_csv('draco_mw.csv')
d['draco_gaia']['ra']=draco.ra
d['draco_gaia']['ra_error']=draco.ra_error
d['draco_gaia']['dec']=draco.dec
d['draco_gaia']['dec_error']=draco.dec_error
d['draco_gaia']['pmra']=draco.pmra
d['draco_gaia']['pmra_error']=draco.pmra_error
d['draco_gaia']['pmdec']=draco.pmdec
d['draco_gaia']['pmdec_error']=draco.pmdec_error
d['draco_gaia']['par']=draco.parallax
d['draco_gaia']['par_error']=draco.parallax_error
d['draco_gaia']['par_over_error']=draco.parallax_over_error
d['draco_gaia']['ra_dec_corr']=draco.ra_dec_corr
d['draco_gaia']['gflux']=draco.phot_g_mean_flux
d['draco_gaia']['gmag']=draco.phot_g_mean_mag
d['draco_gaia']['bpflux']=draco.phot_bp_mean_flux
d['draco_gaia']['bpmag']=draco.phot_bp_mean_mag
d['draco_gaia']['rpflux']=draco.phot_rp_mean_flux
d['draco_gaia']['rpmag']=draco.phot_rp_mean_mag
d['draco_gaia']['bp_rp']=draco.bp_rp
d['draco_gaia']['bp_g']=draco.bp_g
d['draco_gaia']['g_rp']=draco.g_rp
d['draco']['center_ra']=a.ra[0]
d['draco']['center_dec']=a.dec[0]
d['draco']['center_ra_error']=c_ra_e[0]
d['draco']['center_dec_error']=c_dec_e[0]
d['draco']['distance']=b.dis[0]
d['draco']['diameter']=b.dia[0]
d['draco']['avm']=b.avm[0]
d['draco']['mass']=mass[0]
d['draco']['num']=num[0]
d['draco_js']['Mv']=h.Mv[0]
d['draco_js']['Mv_error']=Mv_error[0]
d['draco_js']['r1_2']=h.r1_2[0]
d['draco_js']['r1_2_error']=r1_2_error[0]
d['draco_js']['dist']=h.dist[0]
d['draco_js']['dist_error']=dist_error[0]
d['draco_js']['Vhel']=h.Vhel[0]
d['draco_js']['Vhel_error']=Vhel_error[0]
d['draco_js']['sigma']=h.sigma[0]
d['draco_js']['sigma_error']=sigma_error[0]
d['draco_js']['Fe_H']=h.Fe_H[0]
d['draco_js']['Fe_H_error']=Fe_H_error[0]
d['draco_js']['sigFe_H']=h.sigFe_H[0]
d['draco_js']['sigFe_H_error']=sigFe_H_error[0]
d['draco_mw']['ra']=draco_mw.ra
d['draco_mw']['dec']=draco_mw.dec
d['draco_mw']['Vhel']=draco_mw.Vhel
d['draco_mw']['Vhel_error']=draco_mw.Vhel_error
d['draco_mw']['mem']=draco_mw.mem


carina=pd.read_csv('carina_filtered.csv')
carina_mw=pd.read_csv('carina_mw.csv')
d['carina_gaia']['ra']=carina.ra
d['carina_gaia']['ra_error']=carina.ra_error
d['carina_gaia']['dec']=carina.dec
d['carina_gaia']['dec_error']=carina.dec_error
d['carina_gaia']['pmra']=carina.pmra
d['carina_gaia']['pmra_error']=carina.pmra_error
d['carina_gaia']['pmdec']=carina.pmdec
d['carina_gaia']['pmdec_error']=carina.pmdec_error
d['carina_gaia']['par']=carina.parallax
d['carina_gaia']['par_error']=carina.parallax_error
d['carina_gaia']['par_over_error']=carina.parallax_over_error
d['carina_gaia']['ra_dec_corr']=carina.ra_dec_corr
d['carina_gaia']['gflux']=carina.phot_g_mean_flux
d['carina_gaia']['gmag']=carina.phot_g_mean_mag
d['carina_gaia']['bpflux']=carina.phot_bp_mean_flux
d['carina_gaia']['bpmag']=carina.phot_bp_mean_mag
d['carina_gaia']['rpflux']=carina.phot_rp_mean_flux
d['carina_gaia']['rpmag']=carina.phot_rp_mean_mag
d['carina_gaia']['bp_rp']=carina.bp_rp
d['carina_gaia']['bp_g']=carina.bp_g
d['carina_gaia']['g_rp']=carina.g_rp
d['carina']['center_ra']=a.ra[1]
d['carina']['center_dec']=a.dec[1]
d['carina']['center_ra_error']=c_ra_e[1]
d['carina']['center_dec_error']=c_dec_e[1]
d['carina']['distance']=b.dis[1]
d['carina']['diameter']=b.dia[1]
d['carina']['avm']=b.avm[1]
d['carina']['mass']=mass[1]
d['carina']['num']=num[1]
d['carina_js']['Mv']=fin.Mv[1]
d['carina_js']['Mv_error']=fin.Mv_error[1]
d['carina_js']['r1_2']=fin.r1_2[1]
d['carina_js']['r1_2_error']=fin.r1_2_error[1]
d['carina_js']['dist']=fin.dist[1]
d['carina_js']['dist_error']=fin.dist_error[1]
d['carina_js']['Vhel']=fin.Vhel[1]
d['carina_js']['Vhel_error']=fin.Vhel_error[1]
d['carina_js']['sigma']=fin.sigma[1]
d['carina_js']['sigma_error']=fin.sigma_error[1]
d['carina_js']['Fe_H']=fin.Fe_H[1]
d['carina_js']['Fe_H_error']=fin.Fe_H_error[1]
d['carina_js']['sigFe_H']=fin.sigFe_H[1]
d['carina_js']['sigFe_H_error']=fin.sigFe_H_error[1]
d['carina_mw']['ra']=carina_mw.ra
d['carina_mw']['dec']=carina_mw.dec
d['carina_mw']['Vhel']=carina_mw.Vhel
d['carina_mw']['Vhel_error']=carina_mw.Vhel_error
d['carina_mw']['mem']=carina_mw.mem


umi=pd.read_csv('ursmin_filtered.csv')
umi_mw=pd.read_csv('ursaminor_mw.csv')
d['umi_gaia']['ra']=umi.ra
d['umi_gaia']['ra_error']=umi.ra_error
d['umi_gaia']['dec']=umi.dec
d['umi_gaia']['dec_error']=umi.dec_error
d['umi_gaia']['pmra']=umi.pmra
d['umi_gaia']['pmra_error']=umi.pmra_error
d['umi_gaia']['pmdec']=umi.pmdec
d['umi_gaia']['pmdec_error']=umi.pmdec_error
d['umi_gaia']['par']=umi.parallax
d['umi_gaia']['par_error']=umi.parallax_error
d['umi_gaia']['par_over_error']=umi.parallax_over_error
d['umi_gaia']['ra_dec_corr']=umi.ra_dec_corr
d['umi_gaia']['gflux']=umi.phot_g_mean_flux
d['umi_gaia']['gmag']=umi.phot_g_mean_mag
d['umi_gaia']['bpflux']=umi.phot_bp_mean_flux
d['umi_gaia']['bpmag']=umi.phot_bp_mean_mag
d['umi_gaia']['rpflux']=umi.phot_rp_mean_flux
d['umi_gaia']['rpmag']=umi.phot_rp_mean_mag
d['umi_gaia']['bp_rp']=umi.bp_rp
d['umi_gaia']['bp_g']=umi.bp_g
d['umi_gaia']['g_rp']=umi.g_rp
d['umi']['center_ra']=a.ra[2]
d['umi']['center_dec']=a.dec[2]
d['umi']['center_ra_error']=c_ra_e[2]
d['umi']['center_dec_error']=c_dec_e[2]
d['umi']['distance']=b.dis[2]
d['umi']['diameter']=b.dia[2]
d['umi']['avm']=b.avm[2]
d['umi']['mass']=mass[2]
d['umi']['num']=num[2]
d['umi_js']['Mv']=fin.Mv[2]
d['umi_js']['Mv_error']=fin.Mv_error[2]
d['umi_js']['r1_2']=fin.r1_2[2]
d['umi_js']['r1_2_error']=fin.r1_2_error[2]
d['umi_js']['dist']=fin.dist[2]
d['umi_js']['dist_error']=fin.dist_error[2]
d['umi_js']['Vhel']=fin.Vhel[2]
d['umi_js']['Vhel_error']=fin.Vhel_error[2]
d['umi_js']['sigma']=fin.sigma[2]
d['umi_js']['sigma_error']=fin.sigma_error[2]
d['umi_js']['Fe_H']=fin.Fe_H[2]
d['umi_js']['Fe_H_error']=fin.Fe_H_error[2]
d['umi_js']['sigFe_H']=fin.sigFe_H[2]
d['umi_js']['sigFe_H_error']=fin.sigFe_H_error[2]
d['umi_mw']['ra']=umi_mw.ra
d['umi_mw']['dec']=umi_mw.dec
d['umi_mw']['Vhel']=umi_mw.Vhel
d['umi_mw']['Vhel_error']=umi_mw.Vhel_error
d['umi_mw']['mem']=umi_mw.mem


leo1=pd.read_csv('leo1_filtered.csv')
leo1_mw=pd.read_csv('leo1_mw.csv')
d['leo1_gaia']['ra']=leo1.ra
d['leo1_gaia']['ra_error']=leo1.ra_error
d['leo1_gaia']['dec']=leo1.dec
d['leo1_gaia']['dec_error']=leo1.dec_error
d['leo1_gaia']['pmra']=leo1.pmra
d['leo1_gaia']['pmra_error']=leo1.pmra_error
d['leo1_gaia']['pmdec']=leo1.pmdec
d['leo1_gaia']['pmdec_error']=leo1.pmdec_error
d['leo1_gaia']['par']=leo1.parallax
d['leo1_gaia']['par_error']=leo1.parallax_error
d['leo1_gaia']['par_over_error']=leo1.parallax_over_error
d['leo1_gaia']['ra_dec_corr']=leo1.ra_dec_corr
d['leo1_gaia']['gflux']=leo1.phot_g_mean_flux
d['leo1_gaia']['gmag']=leo1.phot_g_mean_mag
d['leo1_gaia']['bpflux']=leo1.phot_bp_mean_flux
d['leo1_gaia']['bpmag']=leo1.phot_bp_mean_mag
d['leo1_gaia']['rpflux']=leo1.phot_rp_mean_flux
d['leo1_gaia']['rpmag']=leo1.phot_rp_mean_mag
d['leo1_gaia']['bp_rp']=leo1.bp_rp
d['leo1_gaia']['bp_g']=leo1.bp_g
d['leo1_gaia']['g_rp']=leo1.g_rp
d['leo1']['center_ra']=a.ra[3]
d['leo1']['center_dec']=a.dec[3]
d['leo1']['center_ra_error']=c_ra_e[3]
d['leo1']['center_dec_error']=c_dec_e[3]
d['leo1']['distance']=b.dis[3]
d['leo1']['diameter']=b.dia[3]
d['leo1']['avm']=b.avm[3]
d['leo1']['mass']=mass[3]
d['leo1']['num']=num[3]
d['leo1_js']['Mv']=fin.Mv[3]
d['leo1_js']['Mv_error']=fin.Mv_error[3]
d['leo1_js']['r1_2']=fin.r1_2[3]
d['leo1_js']['r1_2_error']=fin.r1_2_error[3]
d['leo1_js']['dist']=fin.dist[3]
d['leo1_js']['dist_error']=fin.dist_error[3]
d['leo1_js']['Vhel']=fin.Vhel[3]
d['leo1_js']['Vhel_error']=fin.Vhel_error[3]
d['leo1_js']['sigma']=fin.sigma[3]
d['leo1_js']['sigma_error']=fin.sigma_error[3]
d['leo1_js']['Fe_H']=fin.Fe_H[3]
d['leo1_js']['Fe_H_error']=fin.Fe_H_error[3]
d['leo1_js']['sigFe_H']=fin.sigFe_H[3]
d['leo1_js']['sigFe_H_error']=fin.sigFe_H_error[3]
d['leo1_mw']['ra']=leo1_mw.ra
d['leo1_mw']['dec']=leo1_mw.dec
d['leo1_mw']['Vhel']=leo1_mw.Vhel
d['leo1_mw']['Vhel_error']=leo1_mw.Vhel_error
d['leo1_mw']['mem']=leo1_mw.mem


leo2=pd.read_csv('leo2_filtered.csv')
leo2_mw=pd.read_csv('leo2_mw.csv')
d['leo2_gaia']['ra']=leo2.ra
d['leo2_gaia']['ra_error']=leo2.ra_error
d['leo2_gaia']['dec']=leo2.dec
d['leo2_gaia']['dec_error']=leo2.dec_error
d['leo2_gaia']['pmra']=leo2.pmra
d['leo2_gaia']['pmra_error']=leo2.pmra_error
d['leo2_gaia']['pmdec']=leo2.pmdec
d['leo2_gaia']['pmdec_error']=leo2.pmdec_error
d['leo2_gaia']['par']=leo2.parallax
d['leo2_gaia']['par_error']=leo2.parallax_error
d['leo2_gaia']['par_over_error']=leo2.parallax_over_error
d['leo2_gaia']['ra_dec_corr']=leo2.ra_dec_corr
d['leo2_gaia']['gflux']=leo2.phot_g_mean_flux
d['leo2_gaia']['gmag']=leo2.phot_g_mean_mag
d['leo2_gaia']['bpflux']=leo2.phot_bp_mean_flux
d['leo2_gaia']['bpmag']=leo2.phot_bp_mean_mag
d['leo2_gaia']['rpflux']=leo2.phot_rp_mean_flux
d['leo2_gaia']['rpmag']=leo2.phot_rp_mean_mag
d['leo2_gaia']['bp_rp']=leo2.bp_rp
d['leo2_gaia']['bp_g']=leo2.bp_g
d['leo2_gaia']['g_rp']=leo2.g_rp
d['leo2']['center_ra']=a.ra[4]
d['leo2']['center_dec']=a.dec[4]
d['leo2']['center_ra_error']=c_ra_e[4]
d['leo2']['center_dec_error']=c_dec_e[4]
d['leo2']['distance']=b.dis[4]
d['leo2']['diameter']=b.dia[4]
d['leo2']['avm']=b.avm[4]
d['leo2']['mass']=mass[4]
d['leo2']['num']=num[4]
d['leo2_js']['Mv']=fin.Mv[4]
d['leo2_js']['Mv_error']=fin.Mv_error[4]
d['leo2_js']['r1_2']=fin.r1_2[4]
d['leo2_js']['r1_2_error']=fin.r1_2_error[4]
d['leo2_js']['dist']=fin.dist[4]
d['leo2_js']['dist_error']=fin.dist_error[4]
d['leo2_js']['Vhel']=fin.Vhel[4]
d['leo2_js']['Vhel_error']=fin.Vhel_error[4]
d['leo2_js']['sigma']=fin.sigma[4]
d['leo2_js']['sigma_error']=fin.sigma_error[4]
d['leo2_js']['Fe_H']=fin.Fe_H[4]
d['leo2_js']['Fe_H_error']=fin.Fe_H_error[4]
d['leo2_js']['sigFe_H']=fin.sigFe_H[4]
d['leo2_js']['sigFe_H_error']=fin.sigFe_H_error[4]
d['leo2_mw']['ra']=leo2_mw.ra
d['leo2_mw']['dec']=leo2_mw.dec
d['leo2_mw']['Vhel']=leo2_mw.Vhel
d['leo2_mw']['Vhel_error']=leo2_mw.Vhel_error
d['leo2_mw']['Fe_H']=leo2_mw.Fe_H
d['leo2_mw']['Fe_H_error']=leo2_mw.Fe_H_error
d['leo2_mw']['mem']=leo2_mw.mem


sextans=pd.read_csv('sextans_filtered.csv')
sextans_mw=pd.read_csv('sextans_mw.csv')
d['sextans_gaia']['ra']=sextans.ra
d['sextans_gaia']['ra_error']=sextans.ra_error
d['sextans_gaia']['dec']=sextans.dec
d['sextans_gaia']['dec_error']=sextans.dec_error
d['sextans_gaia']['pmra']=sextans.pmra
d['sextans_gaia']['pmra_error']=sextans.pmra_error
d['sextans_gaia']['pmdec']=sextans.pmdec
d['sextans_gaia']['pmdec_error']=sextans.pmdec_error
d['sextans_gaia']['par']=sextans.parallax
d['sextans_gaia']['par_error']=sextans.parallax_error
d['sextans_gaia']['par_over_error']=sextans.parallax_over_error
d['sextans_gaia']['ra_dec_corr']=sextans.ra_dec_corr
d['sextans_gaia']['gflux']=sextans.phot_g_mean_flux
d['sextans_gaia']['gmag']=sextans.phot_g_mean_mag
d['sextans_gaia']['bpflux']=sextans.phot_bp_mean_flux
d['sextans_gaia']['bpmag']=sextans.phot_bp_mean_mag
d['sextans_gaia']['rpflux']=sextans.phot_rp_mean_flux
d['sextans_gaia']['rpmag']=sextans.phot_rp_mean_mag
d['sextans_gaia']['bp_rp']=sextans.bp_rp
d['sextans_gaia']['bp_g']=sextans.bp_g
d['sextans_gaia']['g_rp']=sextans.g_rp
d['sextans']['center_ra']=a.ra[5]
d['sextans']['center_dec']=a.dec[5]
d['sextans']['center_ra_error']=c_ra_e[5]
d['sextans']['center_dec_error']=c_dec_e[5]
d['sextans']['distance']=b.dis[5]
d['sextans']['diameter']=b.dia[5]
d['sextans']['avm']=b.avm[5]
d['sextans']['mass']=mass[5]
d['sextans']['num']=num[5]
d['sextans_js']['Mv']=fin.Mv[5]
d['sextans_js']['Mv_error']=fin.Mv_error[5]
d['sextans_js']['r1_2']=fin.r1_2[5]
d['sextans_js']['r1_2_error']=fin.r1_2_error[5]
d['sextans_js']['dist']=fin.dist[5]
d['sextans_js']['dist_error']=fin.dist_error[5]
d['sextans_js']['Vhel']=fin.Vhel[5]
d['sextans_js']['Vhel_error']=fin.Vhel_error[5]
d['sextans_js']['sigma']=fin.sigma[5]
d['sextans_js']['sigma_error']=fin.sigma_error[5]
d['sextans_js']['Fe_H']=fin.Fe_H[5]
d['sextans_js']['Fe_H_error']=fin.Fe_H_error[5]
d['sextans_js']['sigFe_H']=fin.sigFe_H[5]
d['sextans_js']['sigFe_H_error']=fin.sigFe_H_error[5]
d['sextans_mw']['ra']=sextans_mw.ra
d['sextans_mw']['dec']=sextans_mw.dec
d['sextans_mw']['Vhel']=sextans_mw.Vhel
d['sextans_mw']['Vhel_error']=sextans_mw.Vhel_error
d['sextans_mw']['mem']=sextans_mw.mem


fornax=pd.read_csv('fornax_filtered.csv')
fornax_mw=pd.read_csv('fornax_mw.csv')
d['fornax_gaia']['ra']=fornax.ra
d['fornax_gaia']['ra_error']=fornax.ra_error
d['fornax_gaia']['dec']=fornax.dec
d['fornax_gaia']['dec_error']=fornax.dec_error
d['fornax_gaia']['pmra']=fornax.pmra
d['fornax_gaia']['pmra_error']=fornax.pmra_error
d['fornax_gaia']['pmdec']=fornax.pmdec
d['fornax_gaia']['pmdec_error']=fornax.pmdec_error
d['fornax_gaia']['par']=fornax.parallax
d['fornax_gaia']['par_error']=fornax.parallax_error
d['fornax_gaia']['par_over_error']=fornax.parallax_over_error
d['fornax_gaia']['ra_dec_corr']=fornax.ra_dec_corr
d['fornax_gaia']['gflux']=fornax.phot_g_mean_flux
d['fornax_gaia']['gmag']=fornax.phot_g_mean_mag
d['fornax_gaia']['bpflux']=fornax.phot_bp_mean_flux
d['fornax_gaia']['bpmag']=fornax.phot_bp_mean_mag
d['fornax_gaia']['rpflux']=fornax.phot_rp_mean_flux
d['fornax_gaia']['rpmag']=fornax.phot_rp_mean_mag
d['fornax_gaia']['bp_rp']=fornax.bp_rp
d['fornax_gaia']['bp_g']=fornax.bp_g
d['fornax_gaia']['g_rp']=fornax.g_rp
d['fornax']['center_ra']=a.ra[6]
d['fornax']['center_dec']=a.dec[6]
d['fornax']['center_ra_error']=c_ra_e[6]
d['fornax']['center_dec_error']=c_dec_e[6]
d['fornax']['distance']=b.dis[6]
d['fornax']['diameter']=b.dia[6]
d['fornax']['avm']=b.avm[6]
d['fornax']['mass']=mass[6]
d['fornax']['num']=num[6]
d['fornax_js']['Mv']=fin.Mv[6]
d['fornax_js']['Mv_error']=fin.Mv_error[6]
d['fornax_js']['r1_2']=fin.r1_2[6]
d['fornax_js']['r1_2_error']=fin.r1_2_error[6]
d['fornax_js']['dist']=fin.dist[6]
d['fornax_js']['dist_error']=fin.dist_error[6]
d['fornax_js']['Vhel']=fin.Vhel[6]
d['fornax_js']['Vhel_error']=fin.Vhel_error[6]
d['fornax_js']['sigma']=fin.sigma[6]
d['fornax_js']['sigma_error']=fin.sigma_error[6]
d['fornax_js']['Fe_H']=fin.Fe_H[6]
d['fornax_js']['Fe_H_error']=fin.Fe_H_error[6]
d['fornax_js']['sigFe_H']=fin.sigFe_H[6]
d['fornax_js']['sigFe_H_error']=fin.sigFe_H_error[6]
d['fornax_mw']['ra']=fornax_mw.ra
d['fornax_mw']['dec']=fornax_mw.dec
d['fornax_mw']['Vhel']=fornax_mw.Vhel
d['fornax_mw']['Vhel_error']=fornax_mw.Vhel_error
d['fornax_mw']['mem']=fornax_mw.mem


sculptor=pd.read_csv('sculptor_filtered.csv')
sculptor_mw=pd.read_csv('sculptor_mw.csv')
d['sculptor_gaia']['ra']=sculptor.ra
d['sculptor_gaia']['ra_error']=sculptor.ra_error
d['sculptor_gaia']['dec']=sculptor.dec
d['sculptor_gaia']['dec_error']=sculptor.dec_error
d['sculptor_gaia']['pmra']=sculptor.pmra
d['sculptor_gaia']['pmra_error']=sculptor.pmra_error
d['sculptor_gaia']['pmdec']=sculptor.pmdec
d['sculptor_gaia']['pmdec_error']=sculptor.pmdec_error
d['sculptor_gaia']['par']=sculptor.parallax
d['sculptor_gaia']['par_error']=sculptor.parallax_error
d['sculptor_gaia']['par_over_error']=sculptor.parallax_over_error
d['sculptor_gaia']['ra_dec_corr']=sculptor.ra_dec_corr
d['sculptor_gaia']['gflux']=sculptor.phot_g_mean_flux
d['sculptor_gaia']['gmag']=sculptor.phot_g_mean_mag
d['sculptor_gaia']['bpflux']=sculptor.phot_bp_mean_flux
d['sculptor_gaia']['bpmag']=sculptor.phot_bp_mean_mag
d['sculptor_gaia']['rpflux']=sculptor.phot_rp_mean_flux
d['sculptor_gaia']['rpmag']=sculptor.phot_rp_mean_mag
d['sculptor_gaia']['bp_rp']=sculptor.bp_rp
d['sculptor_gaia']['bp_g']=sculptor.bp_g
d['sculptor_gaia']['g_rp']=sculptor.g_rp
d['sculptor']['center_ra']=a.ra[7]
d['sculptor']['center_dec']=a.dec[7]
d['sculptor']['center_ra_error']=c_ra_e[7]
d['sculptor']['center_dec_error']=c_dec_e[7]
d['sculptor']['distance']=b.dis[7]
d['sculptor']['diameter']=b.dia[7]
d['sculptor']['avm']=b.avm[7]
d['sculptor']['mass']=mass[7]
d['sculptor']['num']=num[7]
d['sculptor_js']['Mv']=fin.Mv[7]
d['sculptor_js']['Mv_error']=fin.Mv_error[7]
d['sculptor_js']['r1_2']=fin.r1_2[7]
d['sculptor_js']['r1_2_error']=fin.r1_2_error[7]
d['sculptor_js']['dist']=fin.dist[7]
d['sculptor_js']['dist_error']=fin.dist_error[7]
d['sculptor_js']['Vhel']=fin.Vhel[7]
d['sculptor_js']['Vhel_error']=fin.Vhel_error[7]
d['sculptor_js']['sigma']=fin.sigma[7]
d['sculptor_js']['sigma_error']=fin.sigma_error[7]
d['sculptor_js']['Fe_H']=fin.Fe_H[7]
d['sculptor_js']['Fe_H_error']=fin.Fe_H_error[7]
d['sculptor_js']['sigFe_H']=fin.sigFe_H[7]
d['sculptor_js']['sigFe_H_error']=fin.sigFe_H_error[7]
d['sculptor_mw']['ra']=sculptor_mw.ra
d['sculptor_mw']['dec']=sculptor_mw.dec
d['sculptor_mw']['Vhel']=sculptor_mw.Vhel
d['sculptor_mw']['Vhel_error']=sculptor_mw.Vhel_error
d['sculptor_mw']['mem']=sculptor_mw.mem