# $FreeBSD$

PORTNAME=	palapeli
PORTVERSION=	${KDE4_VERSION}
CATEGORIES=	games kde
MASTER_SITES=	${MASTER_SITE_KDE}
MASTER_SITE_SUBDIR=	${KDE4_BRANCH}/${PORTVERSION}/src
DIST_SUBDIR=	KDE/${PORTVERSION}

MAINTAINER=	kde@FreeBSD.org
COMMENT=	${${PORTNAME}_DESC}

CONFLICTS_INSTALL=	kdegames-4.[0-9].*

USE_KDE4=	kdehier kdelibs kdeprefix libkdegames automoc4
USES=		cmake:outsource shared-mime-info
USE_QT4=	corelib gui gui \
		moc_build qmake_build rcc_build uic_build
USE_XZ=		yes
USE_LDCONFIG=	yes

NO_STAGE=	yes
post-patch:
	${REINPLACE_CMD} -e '/^update_xdg_mimetypes/ d' \
		${WRKSRC}/mime/CMakeLists.txt

.include <${.CURDIR}/../kdegames4/Makefile.common>
.include <bsd.port.mk>
