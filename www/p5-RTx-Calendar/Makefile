# Created by: Matthew Seaman <m.seaman@infracaninophile.co.uk>
# $FreeBSD$

PORTNAME=	RTx-Calendar
PORTVERSION=	0.17
PORTREVISION=	2
CATEGORIES=	www perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	matthew@FreeBSD.org
COMMENT=	Calendar extension module for the RT ticketing system

LICENSE_COMB=   dual
LICENSE=        ART10 GPLv1

BUILD_DEPENDS=	p5-Date-ICal>0:${PORTSDIR}/devel/p5-Date-ICal      \
		p5-Data-ICal>0:${PORTSDIR}/deskutils/p5-Data-ICal  \
		p5-DateTime-Set>0:${PORTSDIR}/devel/p5-DateTime-Set
RUN_DEPENDS:=	${BUILD_DEPENDS}

NO_ARCH=	yes

USES+=		perl5
USE_PERL5=	configure

OPTIONS_SINGLE=			RTVERSION
OPTIONS_SINGLE_RTVERSION=	RT38 RT40 RT42
RT38_DESC=			Install for rt-3.8.x (www/rt38)
RT40_DESC=			Install for rt-4.0.x (www/rt40)
RT42_DESC=			Install for rt-4.2.x (www/rt42)
OPTIONS_DEFAULT=		RT42

.include <bsd.port.options.mk>

.for opt in 38 40 42
.if ${PORT_OPTIONS:MRT${opt}}
RT_VER=		${opt}
.endif
.endfor

BUILD_DEPENDS+=	${LOCALBASE}/bin/rt:${PORTSDIR}/www/rt${RT_VER}
RUN_DEPENDS+=	${LOCALBASE}/bin/rt:${PORTSDIR}/www/rt${RT_VER}

MAN3PREFIX=	${PREFIX}

PLIST_SUB+=	RTHOME=share/rt${RT_VER}

### Temporary for debugging
#WRKDIR=		${WRKDIRPREFIX}${.CURDIR}/work${RT_VER}

post-patch:
	@${FIND} ${WRKSRC} -name '*.orig' -delete

# Note: You can install using an arbitrary $PREFIX but only if it
# matches the $PREFIX used to install www/rt{38,40,42}.  Hence ignore
# $PREFIX in the environment and inherit settings from RT.pm
do-configure:
	@cd ${CONFIGURE_WRKSRC} && \
	    unset PREFIX && \
	    ${SETENV} ${CONFIGURE_ENV} ${PERL5} -I${SITE_PERL} ./${CONFIGURE_SCRIPT} && \
	    ${PERL5} -pi -e 's/ doc_(perl|site|\$$\(INSTALLDIRS\))_install$$//' Makefile

.include <bsd.port.mk>
