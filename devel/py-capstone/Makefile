# Created by: Kubilay Kocak <koobs@FreeBSD.org>
# $FreeBSD$

PORTNAME=	capstone
PORTVERSION=	2.0
PORTREVISION=	1
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DIST_SUBDIR=	python	# Conflicts with devel/capstone distfile

MAINTAINER=	koobs@FreeBSD.org
COMMENT=	Python bindings for the Capstone Disassembly Engine

LICENSE=	BSD3CLAUSE

LIB_DEPENDS=	libcapstone.so:${PORTSDIR}/devel/capstone

USE_PYTHON=		yes
USE_PYDISTUTILS=	yes
PYDISTUTILS_AUTOPLIST=	yes

.include <bsd.port.mk>
