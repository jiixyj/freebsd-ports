# $FreeBSD$

PORTNAME=	kamera
PORTVERSION=	${KDE4_VERSION}
CATEGORIES=	graphics kde
MASTER_SITES=	${MASTER_SITE_KDE}
MASTER_SITE_SUBDIR=	${KDE4_BRANCH}/${PORTVERSION}/src
DIST_SUBDIR=	KDE/${PORTVERSION}

MAINTAINER=	kde@FreeBSD.org
COMMENT=	Digital camera manager for KDE 4

LATEST_LINK=	${PORTNAME}-kde4

LIB_DEPENDS=	libgphoto2.so:${PORTSDIR}/graphics/libgphoto2

CONFLICTS=	kdegraphics-4.[0-6].*

USE_KDE4=	kdehier kdelibs kdeprefix automoc4
USES=		cmake:outsource
USE_QT4=	moc_build qmake_build rcc_build uic_build
USE_XZ=		yes

NO_STAGE=	yes
.include <bsd.port.mk>
