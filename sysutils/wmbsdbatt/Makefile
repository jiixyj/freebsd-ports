# Created by: Josef El-Rayes <josef@FreeBSD.org>
# $FreeBSD$

PORTNAME=	wmbsdbatt
PORTVERSION=	0.1
PORTREVISION=	4
CATEGORIES=	sysutils windowmaker
MASTER_SITES=	http://homepage.univie.ac.at/l.ertl/wmbsdbatt/files/

MAINTAINER=	xride@FreeBSD.org
COMMENT=	Dockapp for battery & temperature monitoring through ACPI

USE_XORG=	x11 xpm

PLIST_FILES=	bin/wmbsdbatt

NO_STAGE=	yes
do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/wmbsdbatt ${PREFIX}/bin

.include <bsd.port.mk>
