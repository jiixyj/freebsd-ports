# Created by: Romain Tartiere <romain@blogreen.org>
# $FreeBSD$

PORTNAME=	paman
PORTVERSION=	0.9.4
PORTREVISION=	4
CATEGORIES=	audio
MASTER_SITES=	http://0pointer.de/lennart/projects/${PORTNAME}/

MAINTAINER=	romain@FreeBSD.org
COMMENT=	Gtk frontend for PulseAudio

LIB_DEPENDS=	libglademm-2.4.so:${PORTSDIR}/devel/libglademm24 \
		libpulse.so:${PORTSDIR}/audio/pulseaudio

GNU_CONFIGURE=	yes
USES=		gmake pathfix pkgconfig
NO_STAGE=	yes

CONFIGURE_ARGS=	--disable-lynx

.include <bsd.port.mk>
