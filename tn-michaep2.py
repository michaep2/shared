#!/usr/bin/env python

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.draw
import cobra.model.fv
import cobra.model.pol
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://cphlab-apic01.cisco.com', 'admin', 'Cisco123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(polUni, ownerKey=u'', name=u'michaep3', descr=u'', ownerTag=u'')
drawCont = cobra.model.draw.Cont(fvTenant)
drawInst = cobra.model.draw.Inst(drawCont, info=u"{'epg-EPG-1':{'x':100,'y':20}}", oDn=u'uni/tn-michaep3/ap-Test-Application')
fvCtx = cobra.model.fv.Ctx(fvTenant, ownerKey=u'', name=u'VRF_1', descr=u'', knwMcastAct=u'permit', ownerTag=u'', pcEnfPref=u'enforced')
fvRsCtxToExtRouteTagPol = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx, tnL3extRouteTagPolName=u'')
fvRsBgpCtxPol = cobra.model.fv.RsBgpCtxPol(fvCtx, tnBgpCtxPolName=u'')
vzAny = cobra.model.vz.Any(fvCtx, matchT=u'AtleastOne', name=u'', descr=u'')
fvRsOspfCtxPol = cobra.model.fv.RsOspfCtxPol(fvCtx, tnOspfCtxPolName=u'')
fvRsCtxToEpRet = cobra.model.fv.RsCtxToEpRet(fvCtx, tnFvEpRetPolName=u'')
fvBD = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'EPG_BD_1', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', limitIpLearnToSubnets=u'no', llAddr=u'::', mac=u'00:22:BD:F8:19:FF', epMoveDetectMode=u'', unicastRoute=u'yes', ownerTag=u'', multiDstPktAct=u'bd-flood', unkMcastAct=u'flood')
fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, tnNdIfPolName=u'')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName=u'VRF_1')
fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, tnIgmpSnoopPolName=u'')
fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, resolveAct=u'resolve', tnFvEpRetPolName=u'')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, tnMonEPGPolName=u'')
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey=u'', prio=u'unspecified', name=u'Test-Application', descr=u'', ownerTag=u'')
fvAEPg = cobra.model.fv.AEPg(fvAp, prio=u'unspecified', matchT=u'AtleastOne', name=u'EPG-1', descr=u'')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, instrImedcy=u'lazy', resImedcy=u'immediate', encap=u'unknown', tDn=u'uni/vmmp-VMware/dom-VMM_ACI_vDVS_1')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=u'EPG_BD_1')
fvCrtrn = cobra.model.fv.Crtrn(fvAEPg, ownerKey=u'', name=u'default', descr=u'', ownerTag=u'')


# commit the generated code to APIC
print toXMLStr(polUni)
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)

