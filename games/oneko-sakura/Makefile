# Created by: HOTARU-YA <hotaru@tail.net>
# $FreeBSD$

PORTNAME=	oneko
PORTVERSION=	1.2
PORTREVISION=	2
CATEGORIES=	games
MASTER_SITES=	http://www.daidouji.com/oneko/distfiles/
DISTNAME=	${PORTNAME}-${PORTVERSION}.sakura.5
PKGNAMESUFFIX=	-sakura

MAINTAINER=	hotaru@tail.net
COMMENT=	A cat, Sakura or Tomoyo chasing a mouse all over the screen

CONFLICTS=	oneko-2.*

USES=		imake
USE_XORG=	x11 xext
MAN6=		oneko.6
PLIST_FILES=	bin/oneko
NO_CDROM=	Including derivatives from CARDCAPTOR SAKURA. See http://www.clamp-net.com/ -> INFORMATION

NO_STAGE=	yes
pre-configure:
	@${REINPLACE_CMD} -e 's,/\*\*/# Cannot compile in using Gcc,/* Cannot compile using Gcc */,' \
		${WRKSRC}/Imakefile
	@${ECHO_CMD} "MANSUFFIX=6" >>${WRKSRC}/Imakefile

post-configure:
	@${REINPLACE_CMD} -e 's,^all:: oneko\..*\.html$$,,' \
			  -e 's,^install.man:: oneko\..*\.html$$,do-nada:,' \
		${WRKSRC}/Makefile

.include <bsd.port.mk>
