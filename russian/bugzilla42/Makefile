# $FreeBSD$

PORTNAME=	bugzilla
PORTVERSION=	4.2.7
CATEGORIES=	russian
MASTER_SITES=	SF
MASTER_SITE_SUBDIR=bugzilla-ru/bugzilla-${PORTVERSION:R}-ru/${PORTVERSION}
DISTNAME=	bugzilla-${PORTVERSION}-ru-20131125

MAINTAINER=	bugzilla@FreeBSD.org
COMMENT=	Russian localization for Bugzilla

RUN_DEPENDS=	bugzilla42>=${PORTVERSION}:${PORTSDIR}/devel/bugzilla42

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}.ru

.include "${.CURDIR}/../../devel/bugzilla42/Makefile.common"

do-install:
	${MKDIR} ${STAGEDIR}${WWWDIR}
	(cd ${WRKSRC}/ && ${PAX} -r -w * ${STAGEDIR}${WWWDIR})

# Maintainer
plist:	patch
	@( cd ${WRKSRC}/ && ${FIND} * -type f | ${AWK} '{print "%%WWWDIR%%/"$$1}' | ${SORT} > ${PLIST}.new )
	@( cd ${WRKSRC}/ && ${FIND} * -type d | ${AWK} '{print "@dirrmtry %%WWWDIR%%/"$$1}' | ${SORT} -r >> ${PLIST}.new )
	@if ${DIFF} -u ${PLIST} ${PLIST}.new ; then \
		${ECHO_MSG} no pkg-plist changes; \
		${RM} ${PLIST}.new ; \
	fi

.include <bsd.port.mk>
