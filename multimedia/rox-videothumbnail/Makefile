# $FreeBSD$

PORTNAME=	rox-videothumbnail
PORTVERSION=	0.1.14
PORTREVISION=	3
CATEGORIES=	multimedia
MASTER_SITES=	http://www.kerofin.demon.co.uk/rox/
DISTNAME=	VideoThumbnail-${PORTVERSION}

MAINTAINER=	olgeni@FreeBSD.org
COMMENT=	Video thumbnail provider for the ROX file manager

RUN_DEPENDS=	${LOCALBASE}/bin/rox:${PORTSDIR}/x11-fm/rox-filer \
		${LOCALBASE}/lib/ROX-Lib2/python/rox/__init__.py:${PORTSDIR}/devel/py-roxlib

WRKSRC=		${WRKDIR}/VideoThumbnail

USE_PYTHON=	yes

NO_STAGE=	yes
do-build:
	@${PYTHON_CMD} -m compileall ${WRKSRC}
	@${PYTHON_CMD} -O -m compileall ${WRKSRC}

do-install:
	@${MKDIR} ${PREFIX}/apps
	@${CP} -r ${WRKSRC} ${PREFIX}/apps/
	@${CHOWN} -R ${SHAREOWN}:${SHAREGRP} ${PREFIX}/apps/VideoThumbnail

.include <bsd.port.mk>
