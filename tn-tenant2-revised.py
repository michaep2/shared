#!/usr/bin/env python

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.draw
import cobra.model.fv
import cobra.model.l3ext
import cobra.model.ospf
import cobra.model.pol
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://10.54.61.56', 'admin', 'Cisco123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(polUni, ownerKey=u'', name=u'tenant2', descr=u'', ownerTag=u'')
vzBrCP = cobra.model.vz.BrCP(fvTenant, ownerKey=u'', name=u'Con_ICMP', prio=u'unspecified', ownerTag=u'', descr=u'')
vzSubj = cobra.model.vz.Subj(vzBrCP, revFltPorts=u'yes', name=u'Sub_ICMP', prio=u'unspecified', descr=u'', consMatchT=u'AtleastOne', provMatchT=u'AtleastOne')
vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, tnVzFilterName=u'icmp')
vzBrCP2 = cobra.model.vz.BrCP(fvTenant, ownerKey=u'', name=u'Con_HTTP', prio=u'unspecified', ownerTag=u'', descr=u'')
vzSubj2 = cobra.model.vz.Subj(vzBrCP2, revFltPorts=u'yes', name=u'Sub_HTTP', prio=u'unspecified', descr=u'', consMatchT=u'AtleastOne', provMatchT=u'AtleastOne')
vzRsSubjFiltAtt2 = cobra.model.vz.RsSubjFiltAtt(vzSubj2, tnVzFilterName=u'http')
drawCont = cobra.model.draw.Cont(fvTenant)
drawInst = cobra.model.draw.Inst(drawCont, info=u"{'epg-EPG-1':{'x':100,'y':20}}", oDn=u'uni/tn-tenant2/ap-test-application1')
fvCtx = cobra.model.fv.Ctx(fvTenant, ownerKey=u'', name=u'VRF_1', descr=u'', knwMcastAct=u'permit', ownerTag=u'', pcEnfPref=u'enforced')
fvRsCtxToExtRouteTagPol = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx, tnL3extRouteTagPolName=u'')
fvRsBgpCtxPol = cobra.model.fv.RsBgpCtxPol(fvCtx, tnBgpCtxPolName=u'')
vzAny = cobra.model.vz.Any(fvCtx, matchT=u'AtleastOne', name=u'', descr=u'')
fvRsOspfCtxPol = cobra.model.fv.RsOspfCtxPol(fvCtx, tnOspfCtxPolName=u'')
fvRsCtxToEpRet = cobra.model.fv.RsCtxToEpRet(fvCtx, tnFvEpRetPolName=u'')
fvBD = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'BD_10-54-62-145_29', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', limitIpLearnToSubnets=u'yes', llAddr=u'::', mac=u'00:22:BD:F8:19:FF', epMoveDetectMode=u'', unicastRoute=u'yes', ownerTag=u'', multiDstPktAct=u'bd-flood', unkMcastAct=u'flood')
fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, tnNdIfPolName=u'')
fvRsBDToOut = cobra.model.fv.RsBDToOut(fvBD, tnL3extOutName=u'L3out_External_VRF_1')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName=u'VRF_1')
fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, tnIgmpSnoopPolName=u'')
fvSubnet = cobra.model.fv.Subnet(fvBD, name=u'', descr=u'', ctrl=u'querier', scope=u'public', ip=u'10.54.62.145/29', preferred=u'no')
fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, resolveAct=u'resolve', tnFvEpRetPolName=u'')
fvBD2 = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'BD_L3_10-54-63-10_31', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', limitIpLearnToSubnets=u'no', llAddr=u'::', mac=u'00:22:BD:F8:19:FF', epMoveDetectMode=u'', unicastRoute=u'yes', ownerTag=u'', multiDstPktAct=u'bd-flood', unkMcastAct=u'flood')
fvRsBDToNdP2 = cobra.model.fv.RsBDToNdP(fvBD2, tnNdIfPolName=u'')
fvRsBDToOut2 = cobra.model.fv.RsBDToOut(fvBD2, tnL3extOutName=u'L3out_External_VRF_1')
fvRsCtx2 = cobra.model.fv.RsCtx(fvBD2, tnFvCtxName=u'VRF_1')
fvRsIgmpsn2 = cobra.model.fv.RsIgmpsn(fvBD2, tnIgmpSnoopPolName=u'')
fvRsBdToEpRet2 = cobra.model.fv.RsBdToEpRet(fvBD2, resolveAct=u'resolve', tnFvEpRetPolName=u'')
fvBD3 = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'BD_10-54-62-153_29', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', limitIpLearnToSubnets=u'yes', llAddr=u'::', mac=u'00:22:BD:F8:19:FF', epMoveDetectMode=u'', unicastRoute=u'yes', ownerTag=u'', multiDstPktAct=u'bd-flood', unkMcastAct=u'flood')
fvRsBDToNdP3 = cobra.model.fv.RsBDToNdP(fvBD3, tnNdIfPolName=u'')
fvRsBDToOut3 = cobra.model.fv.RsBDToOut(fvBD3, tnL3extOutName=u'L3out_External_VRF_1')
fvRsCtx3 = cobra.model.fv.RsCtx(fvBD3, tnFvCtxName=u'VRF_1')
fvRsIgmpsn3 = cobra.model.fv.RsIgmpsn(fvBD3, tnIgmpSnoopPolName=u'')
fvSubnet2 = cobra.model.fv.Subnet(fvBD3, name=u'', descr=u'', ctrl=u'querier', scope=u'public', ip=u'10.54.62.153/29', preferred=u'no')
fvRsBdToEpRet3 = cobra.model.fv.RsBdToEpRet(fvBD3, resolveAct=u'resolve', tnFvEpRetPolName=u'')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, tnMonEPGPolName=u'')
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey=u'', prio=u'unspecified', name=u'test-application1', descr=u'', ownerTag=u'')
fvAEPg = cobra.model.fv.AEPg(fvAp, prio=u'unspecified', matchT=u'AtleastOne', name=u'EPG-2', descr=u'')
fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'Con_HTTP', prio=u'unspecified')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'Con_ICMP', prio=u'unspecified')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, instrImedcy=u'lazy', resImedcy=u'immediate', encap=u'unknown', tDn=u'uni/vmmp-VMware/dom-VMM_ACI_vDVS_1')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=u'BD_10-54-62-153_29')
fvCrtrn = cobra.model.fv.Crtrn(fvAEPg, ownerKey=u'', name=u'default', descr=u'', ownerTag=u'')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, prio=u'unspecified', matchT=u'AtleastOne', name=u'EPG-1', descr=u'')
fvRsCons3 = cobra.model.fv.RsCons(fvAEPg2, tnVzBrCPName=u'Con_HTTP', prio=u'unspecified')
fvRsCons4 = cobra.model.fv.RsCons(fvAEPg2, tnVzBrCPName=u'Con_ICMP', prio=u'unspecified')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, instrImedcy=u'lazy', resImedcy=u'immediate', encap=u'unknown', tDn=u'uni/vmmp-VMware/dom-VMM_ACI_vDVS_1')
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, tnQosCustomPolName=u'')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=u'BD_10-54-62-145_29')
fvCrtrn2 = cobra.model.fv.Crtrn(fvAEPg2, ownerKey=u'', name=u'default', descr=u'', ownerTag=u'')
ospfIfPol = cobra.model.ospf.IfPol(fvTenant, nwT=u'p2p', ownerKey=u'', name=u'IntPol_OSPF_P2P', descr=u'', ctrl=u'', helloIntvl=u'10', rexmitIntvl=u'5', xmitDelay=u'1', cost=u'unspecified', ownerTag=u'', prio=u'1', deadIntvl=u'40')
l3extOut = cobra.model.l3ext.Out(fvTenant, ownerKey=u'', name=u'L3out_External_VRF_1', descr=u'', targetDscp=u'unspecified', enforceRtctrl=u'export', ownerTag=u'')
l3extRsEctx = cobra.model.l3ext.RsEctx(l3extOut, tnFvCtxName=u'VRF_1')
l3extLNodeP = cobra.model.l3ext.LNodeP(l3extOut, ownerKey=u'', name=u'NP_Leaf101', descr=u'', targetDscp=u'unspecified', tag=u'yellow-green', ownerTag=u'')
l3extRsNodeL3OutAtt = cobra.model.l3ext.RsNodeL3OutAtt(l3extLNodeP, rtrIdLoopBack=u'yes', rtrId=u'222.222.222.222', tDn=u'topology/pod-1/node-101')
l3extLoopBackIfP = cobra.model.l3ext.LoopBackIfP(l3extRsNodeL3OutAtt, addr=u'222.222.222.222', descr=u'', name=u'')
l3extLIfP = cobra.model.l3ext.LIfP(l3extLNodeP, ownerKey=u'', tag=u'yellow-green', name=u'IntProf_OSPF', descr=u'', ownerTag=u'')
ospfIfP = cobra.model.ospf.IfP(l3extLIfP, authKeyId=u'1', authType=u'none', name=u'', descr=u'')
ospfRsIfPol = cobra.model.ospf.RsIfPol(ospfIfP, tnOspfIfPolName=u'IntPol_OSPF_P2P')
l3extRsNdIfPol = cobra.model.l3ext.RsNdIfPol(l3extLIfP, tnNdIfPolName=u'default')
l3extRsPathL3OutAtt = cobra.model.l3ext.RsPathL3OutAtt(l3extLIfP, addr=u'10.54.63.10/31', descr=u'', targetDscp=u'unspecified', llAddr=u'::', mac=u'00:22:BD:F8:19:FF', mode=u'regular', encap=u'vlan-1152', ifInstT=u'sub-interface', mtu=u'9000', tDn=u'topology/pod-1/paths-101/pathep-[eth1/48]')
l3extRsL3DomAtt = cobra.model.l3ext.RsL3DomAtt(l3extOut, tDn=u'uni/l3dom-L3dom_External')
l3extInstP = cobra.model.l3ext.InstP(l3extOut, prio=u'unspecified', matchT=u'AtleastOne', name=u'Ext_L3_OSPF', descr=u'', targetDscp=u'unspecified')
l3extSubnet = cobra.model.l3ext.Subnet(l3extInstP, aggregate=u'', ip=u'0.0.0.0/0', name=u'', descr=u'')
fvRsCustQosPol3 = cobra.model.fv.RsCustQosPol(l3extInstP, tnQosCustomPolName=u'')
fvRsProv = cobra.model.fv.RsProv(l3extInstP, tnVzBrCPName=u'Con_HTTP', matchT=u'AtleastOne', prio=u'unspecified')
fvRsProv2 = cobra.model.fv.RsProv(l3extInstP, tnVzBrCPName=u'Con_ICMP', matchT=u'AtleastOne', prio=u'unspecified')
ospfExtP = cobra.model.ospf.ExtP(l3extOut, areaCtrl=u'redistribute,summary', areaId=u'backbone', areaType=u'regular', areaCost=u'1', descr=u'')


# commit the generated code to APIC
print toXMLStr(polUni)
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)

