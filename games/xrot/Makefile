# Created by: Mark Pulford <mark@kyne.com.au>
# $FreeBSD$

PORTNAME=	xrot
PORTVERSION=	1.3.2
PORTREVISION=	1
CATEGORIES=	games
MASTER_SITES=	http://hanzubon.jp/mirrors/Vine/%SUBDIR%/ \
		http://ftp.jaist.ac.jp/pub/Linux/Vine/%SUBDIR%/ \
		http://ftp.riken.go.jp/Linux/vine/%SUBDIR%/ \
		http://ftp.yz.yamagata-u.ac.jp/pub/Linux/Vine/%SUBDIR%/ \
		http://ftp.nara.wide.ad.jp/pub/Linux/vine/%SUBDIR%/ \
		http://ftp.vinelinux.org/pub/Vine/%SUBDIR%/
MASTER_SITE_SUBDIR=	VinePlus/1.1/JG-0.9.1/sources

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Falling ball puzzle game for X

WRKSRC=		${WRKDIR}/xrot

USES=		imake
USE_XORG=	xpm
ALL_TARGET=	xrot
CFLAGS+=	-Wno-return-type

PLIST_FILES=	bin/xrot

NO_STAGE=	yes
do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/xrot ${PREFIX}/bin
	${CHOWN} root:games ${PREFIX}/bin/xrot
	${CHMOD} g+s ${PREFIX}/bin/xrot
	${SH} pkg-install ${PKGNAME} POST-INSTALL

.include <bsd.port.mk>
