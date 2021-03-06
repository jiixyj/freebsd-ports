# Created by: Michael Johnson <ahze@FreeBSD.org>
# $FreeBSD$

PORTNAME=	dejavu
PORTVERSION=	2.34
CATEGORIES=	x11-fonts
MASTER_SITES=	SF
DISTNAME=	${PORTNAME}-fonts-ttf-${PORTVERSION}

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Bitstream Vera Fonts clone with a wider range of characters

BUILD_DEPENDS=	fc-cache:${PORTSDIR}/x11-fonts/fontconfig
RUN_DEPENDS:=	${BUILD_DEPENDS}

OPTIONS_DEFINE=	DOCS LINKS
LINKS_DESC=	Install links of configuration files in conf.d

NO_BUILD=	yes
USE_BZIP2=	yes

FCDIR=		${PREFIX}/${FCDIR_REL}
FCDIR_REL?=	etc/fonts/conf.avail
FONTSDIR=	${PREFIX}/${FONTSDIR_REL}
FONTSDIR_REL?=	lib/X11/fonts/${PORTNAME}
PLIST_SUB=	FCDIR_REL=${FCDIR_REL} FONTSDIR_REL=${FONTSDIR_REL}
PORTDOCS=	README langcover.txt status.txt unicover.txt
SUB_FILES=	pkg-message
SUB_LIST=	FONTSDIR=${FONTSDIR}

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MLINKS}
FCDIR_LINKS=	${FCDIR_REL:S|conf.avail|conf.d|}
PLIST_SUB+=	FCDIR_LINKS="${FCDIR_LINKS}"
.else
PLIST_SUB+=	FCDIR_LINKS="@comment "
.endif

do-install:
	${MKDIR} ${STAGEDIR}${FCDIR} ${STAGEDIR}${FONTSDIR}/
	${INSTALL_DATA} ${WRKSRC}/fontconfig/*.conf ${STAGEDIR}${FCDIR}/
	${INSTALL_DATA} ${WRKSRC}/ttf/*.ttf ${STAGEDIR}${FONTSDIR}/
.if ${PORT_OPTIONS:MDOCS}
	${MKDIR} ${STAGEDIR}${DOCSDIR}/
	cd ${WRKSRC} && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}/
.endif
.if ${PORT_OPTIONS:MLINKS}
	cd ${STAGEDIR}${PREFIX}/${FCDIR_LINKS}/ && ${LN} -fs ../conf.avail/*dejavu*.conf .
.endif
	@${ECHO_MSG} "===> Running fc-cache"
	-${LOCALBASE}/bin/fc-cache -f -v ${FONTSDIR}/
	@${ECHO_MSG}

.include <bsd.port.mk>
