# Created by: Olivier Duchateau
# $FreeBSD$

PORTNAME=	itsdangerous
PORTVERSION=	0.23
CATEGORIES=	security python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	olivierd@FreeBSD.org
COMMENT=	Various helpers to pass data in untrusted environments

USE_PYTHON=	yes
USE_PYDISTUTILS=	yes
PYDISTUTILS_AUTOPLIST=	yes

OPTIONSFILE=	${PORT_DBDIR}/py-${PORTNAME}/options
OPTIONS_DEFINE=	JSON

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MJSON}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}simplejson>=3.0:${PORTSDIR}/devel/py-simplejson
.endif

.include <bsd.port.mk>
