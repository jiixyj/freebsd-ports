# Created by: Yoichi NAKAYAMA <yoichi@eken.phys.nagoya-u.ac.jp>
# $FreeBSD$

PORTNAME=	marumoji-fonts
PORTVERSION=	1.0
PORTREVISION=	5
CATEGORIES=	japanese x11-fonts
MASTER_SITES=	${MASTER_SITE_LOCAL}
MASTER_SITE_SUBDIR=	yoichi
DISTFILES=	maru14.bdf.v13.gz maru18.bdf.v10.gz \
		m18to16.sed \
		7x14maru.bdf.gz 7x14rkmr.bdf.gz \
		8x16maru.bdf.gz 8x16rkmr.bdf.gz \
		9x18maru.bdf.gz 9x18rkmr.bdf.gz
DIST_SUBDIR=	${PORTNAME}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Japanese marumoji fonts

BUILD_DEPENDS=	mkbold:${PORTSDIR}/x11-fonts/mkbold-mkitalic \
		bdftopcf:${PORTSDIR}/x11-fonts/bdftopcf
RUN_DEPENDS=	mkfontdir:${PORTSDIR}/x11-fonts/mkfontdir \
		mkfontscale:${PORTSDIR}/x11-fonts/mkfontscale

NO_WRKSUBDIR=	yes
FONTSDIR=	lib/X11/fonts/local

NO_STAGE=	yes
.include <bsd.port.pre.mk>

EXTRACT_CMD=		${CP}
EXTRACT_BEFORE_ARGS=	-p
EXTRACT_AFTER_ARGS=	${WRKDIR}

MAKE_ENV=	FONTSDIR=${FONTSDIR}
PLIST_SUB=	FONTSDIR=${FONTSDIR}

post-extract:
	@${MV} ${WRKDIR}/maru14.bdf.v13.gz ${WRKDIR}/maru14.bdf.gz
	@${MV} ${WRKDIR}/maru18.bdf.v10.gz ${WRKDIR}/maru18.bdf.gz
	@${CP} ${FILESDIR}/Makefile.in ${WRKDIR}/Makefile
	@(cd ${WRKDIR}; ${GUNZIP_CMD} *.gz)

pre-build:
	@(cd ${WRKDIR}; ${SED} -f m18to16.sed < maru18.bdf > maru16.bdf)
pre-su-install:
	@${SETENV} PKG_PREFIX=${PREFIX} \
		${SH} ${PKGREQ} ${PKGNAME} INSTALL

post-install:
	@(cd ${PREFIX}/${FONTSDIR}; mkfontdir)
	${MKDIR} ${PREFIX}/share/doc/marumoji-fonts
	${INSTALL_DATA} ${FILESDIR}/LICENSE ${PREFIX}/share/doc/marumoji-fonts

.include <bsd.port.post.mk>
