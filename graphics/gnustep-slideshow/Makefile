# $FreeBSD$

PORTNAME=	slideshow
PORTVERSION=	0.3.5
PORTREVISION=	2
CATEGORIES=	graphics gnustep
MASTER_SITES=	http://download.gna.org/gsimageapps/
PKGNAMEPREFIX=	gnustep-
DISTNAME=	SlideShow-${PORTVERSION}

MAINTAINER=	theraven@FreeBSD.org
COMMENT=	SlideShow Viewer

LICENSE=	GPLv2

USE_BZIP2=	yes
USE_GNUSTEP=	yes
USE_GNUSTEP_BACK=	yes
USE_GNUSTEP_BUILD=	yes
USE_GNUSTEP_INSTALL=	yes
USE_GNUSTEP_LOCAL_LIBS+=	SlideShow:${SLIDESHOWKIT_PORT}

OBJCFLAGS+=	-Dsel_eq=sel_isEqual

SLIDESHOWKIT_PORT?=	graphics/gnustep-slideshowkit

NO_STAGE=	yes
.include <bsd.port.mk>
