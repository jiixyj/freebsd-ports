# Created by: Ed Schouten <ed@FreeBSD.org>
# $FreeBSD$

PORTNAME=	libxspf
PORTVERSION=	1.2.0
CATEGORIES=	multimedia
MASTER_SITES=	SF/libspiff/Sources/${PORTVERSION}

MAINTAINER=	ed@FreeBSD.org
COMMENT=	An XSPF parsing library

LIB_DEPENDS=	expat.6:${PORTSDIR}/textproc/expat2

# We need 0.7.5, which uses pkg-config
BUILD_DEPENDS=	uriparser>=0.7.5:${PORTSDIR}/net/uriparser
RUN_DEPENDS=	uriparser>=0.7.5:${PORTSDIR}/net/uriparser

GNU_CONFIGURE=	yes
CONFIGURE_ARGS+=--with-expat=${LOCALBASE} --disable-test

USE_BZIP2=	yes
USES=		pkgconfig
USE_AUTOTOOLS=	libtool
USE_LDCONFIG=	yes

post-patch:
	@${REINPLACE_CMD} 's|$$(libdir)/pkgconfig|$$(libdir)data/pkgconfig|' \
	    ${WRKSRC}/Makefile.in

.include <bsd.port.mk>
