# Created by: Donald Burr <dburr@FreeBSD.org>
# $FreeBSD$

PORTNAME=	yodl
PORTVERSION=	3.03.0
CATEGORIES=	textproc
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTVERSION}
DISTNAME=	${PORTNAME}_${PORTVERSION}
EXTRACT_SUFX=	.orig.tar.gz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Easy to use but powerful document formatting/preparation language

RUN_DEPENDS=	bash:${PORTSDIR}/shells/bash \
		${LOCALBASE}/bin/getopt:${PORTSDIR}/misc/getopt
BUILD_DEPENDS=	icmake:${PORTSDIR}/devel/icmake \
		bash:${PORTSDIR}/shells/bash \
		gsed:${PORTSDIR}/textproc/gsed

USES=		perl5
USE_PERL5=	build

DOCSDIR=	${PREFIX}/share/doc/${PORTNAME}-${PORTVERSION}
PORTDOCS=	*

PLIST_SUB+=	PORTVERSION="${PORTVERSION}"

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MDOCS}
USE_TEX=	latex:build dvipsk:build
.endif

USES=		shebangfix

SHEBANG_LANG=	icmake
icmake_OLD_CMD=	/usr/bin/icmake
icmake_CMD=	${LOCALBASE}/bin/icmake

SHEBANG_FILES=	${WRKSRC}/macros/rawmacros/create \
		${WRKSRC}/macros/rawmacros/keepdiff \
		${WRKSRC}/macros/rawmacros/makeyoin \
		${WRKSRC}/macros/rawmacros/repairs \
		${WRKSRC}/macros/rawmacros/separator \
		${WRKSRC}/macros/rawmacros/separator.pl \
		${WRKSRC}/macros/rawmacros/startdoc \
		${WRKSRC}/macros/rawmacros/startdoc.pl \
		${WRKSRC}/contrib/build.pl \
		${WRKSRC}/src/yodl/replace \
		${WRKSRC}/scripts/configreplacements \
		${WRKSRC}/scripts/macroseparator.pl \
		${WRKSRC}/scripts/stdmacros \
		${WRKSRC}/scripts/yodl2whatever.in \
		${WRKSRC}/build

post-patch:
	@${REINPLACE_CMD} -e 's|"/usr"|"${PREFIX}"| ; \
		s|"/share/yodl"|"/share/${PORTNAME}-${PORTVERSION}"| ; \
		s|"/share/man"|"/man"| ; \
		s|"/share/doc/yodl"|"/share/doc/${PORTNAME}-${PORTVERSION}"| ; \
		s|"/share/doc/yodl-doc"|"/share/doc/${PORTNAME}-${PORTVERSION}/doc"| ; \
		s|"gcc"|"${CC}"|' \
		${WRKSRC}/INSTALL.im
	@${REINPLACE_CMD} -e 's|yodlconverters.1|yodlconverters.1.gz| ; \
		s|".1"|".1.gz"|' \
		${WRKSRC}/icmake/install
	@${REINPLACE_CMD} -e 's|#!/usr/bin/icmake|#!${LOCALBASE}/bin/icmake| ; \
		s|"-O2 -Wall"|"-Wall ${CFLAGS}"|' \
		${WRKSRC}/build
	@${REINPLACE_CMD} -e 's|sed |${LOCALBASE}/bin/gsed | ; \
		s|getopt |${LOCALBASE}/bin/getopt |' \
		${WRKSRC}/scripts/configreplacements \
		${WRKSRC}/scripts/yodl2whatever.in \
		${WRKSRC}/scripts/yodlstriproff \
		${WRKSRC}/macros/rawmacros/repairs

do-build:
	@cd ${WRKSRC} && ./build programs strip
	@cd ${WRKSRC} && ./build macros
	@cd ${WRKSRC} && ./build man
.if ${PORT_OPTIONS:MDOCS}
	@cd ${WRKSRC} && ./build manual
.endif

do-install:
	@cd ${WRKSRC} && ./build install programs ${STAGEDIR}
	@cd ${WRKSRC} && ./build install macros ${STAGEDIR}
	@cd ${WRKSRC} && ./build install man ${STAGEDIR}
.if ${PORT_OPTIONS:MDOCS}
	@cd ${WRKSRC} && ./build install manual ${STAGEDIR}
	@cd ${WRKSRC} && ./build install docs ${STAGEDIR}
.endif

.include <bsd.port.mk>
