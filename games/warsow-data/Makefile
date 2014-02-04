# Created by: Jose Alonso Cardenas Marquez <acm@FreeBSD.org>
# $FreeBSD$

PORTNAME=	data
PORTVERSION=	1.0.2
CATEGORIES=	games
MASTER_SITES=	SF/warsow.mirror/Warsow%20${PORTVERSION:R}${PORTVERSION:E}/ \
		http://www.zcdn.org/dl/${PORTVERSION:R}${PORTVERSION:E}/ \
		http://wsw.null.so/ \
		http://www.warsow.net:1337/~warsow/${PORTVERSION:R}${PORTVERSION:E}/
PKGNAMEPREFIX=	warsow-
DISTNAME=	${PKGNAMEPREFIX:S/-//}_${PORTVERSION:R}${PORTVERSION:E}
DIST_SUBDIR=	${PKGNAMEPREFIX:S/-//}

MAINTAINER=	acm@FreeBSD.org
COMMENT=	Warsow data files

LICENSE=	WARSOW GPLv2
LICENSE_COMB=	multi
LICENSE_NAME_WARSOW=	Warsow Content License
LICENSE_FILE_WARSOW=	${WRKSRC}/docs/license.txt
LICENSE_PERMS_WARSOW=	pkg-mirror dist-mirror

# Package size below is for default set of OPTIONS
NO_PACKAGE=	Package will be 493MB, set FORCE_PACKAGE if you really want it

# Game port is restricted to these architectures, so it makes no sense to
# package game data port as well (even it is not being technically built)
ONLY_FOR_ARCHS=	i386 amd64

NO_BUILD=	yes
DATADIR=	${PREFIX}/share/${PKGNAMEPREFIX:S/-//}
DOCSDIR=	${PREFIX}/share/doc/${PKGNAMEPREFIX:S/-//}
TXTDOCS=	bots_navigation.txt changelog.txt contact.txt \
		dedicated_server_quide.txt demoavi.txt democams.txt \
		features.txt huds.txt license.txt linux_sound_sdl.txt \
		mousefilter.txt old_changelog.txt query_protocols.txt
PORTDOCS=	0.4_renderer_changes.png ${TXTDOCS}

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

pre-patch:
	${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} ${WRKSRC}/basewsw/ui_porkui.pk3     -C ${WRKSRC}/basewsw ${EXTRACT_AFTER_ARGS}
	${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} ${WRKSRC}/basewsw/ui_porkui_001.pk3 -C ${WRKSRC}/basewsw ${EXTRACT_AFTER_ARGS}
	${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} ${WRKSRC}/basewsw/ui_porkui_002.pk3 -C ${WRKSRC}/basewsw ${EXTRACT_AFTER_ARGS}

do-install:
	@${MKDIR} ${STAGEDIR}${DATADIR}
	cd ${WRKSRC} && ${COPYTREE_SHARE} basewsw ${STAGEDIR}${DATADIR}
.if ${PORT_OPTIONS:MDOCS}
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	cd ${WRKSRC}/docs && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
