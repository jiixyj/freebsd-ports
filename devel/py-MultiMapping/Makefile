# $FreeBSD$

PORTNAME=	MultiMapping
PORTVERSION=	2.13.0
PORTREVISION=	1
CATEGORIES=	devel python zope
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DIST_SUBDIR=	zope

MAINTAINER=	zope@FreeBSD.org
COMMENT=	Special MultiMapping objects used in Zope2

LICENSE=	ZPL21

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ExtensionClass>=0:${PORTSDIR}/devel/py-ExtensionClass

USE_PYTHON=		yes
USE_PYDISTUTILS=	yes
PYDISTUTILS_AUTOPLIST=	yes
USE_ZIP=		yes

.include <bsd.port.mk>
