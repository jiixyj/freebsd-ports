# Created by: Andreas Kohn <andreas@syndrom23.de>
# $FreeBSD$

PORTNAME=	mksh
DISTVERSION=	R49
PORTREVISION=	1
CATEGORIES=	shells
MASTER_SITES=	http://www.mirbsd.org/MirOS/dist/mir/mksh/ \
		http://pub.allbsd.org/MirOS/dist/mir/mksh/
DISTFILES=	${PORTNAME}-${DISTVERSION}.tgz

MAINTAINER=	miwi@FreeBSD.org
COMMENT=	MirBSD Korn Shell

WRKSRC=		${WRKDIR}/${PORTNAME}

.include <bsd.port.options.mk>

do-build:
	cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} SHELL=${SH} ${SH} ${WRKSRC}/Build.sh -r -c lto

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/mksh ${STAGEDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/mksh.1 ${STAGEDIR}${MANPREFIX}/man/man1
.if ${PORT_OPTIONS:MEXAMPLES}
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	${INSTALL_DATA} ${WRKSRC}/dot.mkshrc ${STAGEDIR}${EXAMPLESDIR}
.endif

.include <bsd.port.mk>
