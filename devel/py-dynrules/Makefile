# $FreeBSD$

PORTNAME=	dynrules
PORTVERSION=	0.1.0
PORTREVISION=	1
CATEGORIES=	devel python
MASTER_SITES=	http://cdn.bitbucket.org/marcusva/py-dynrules/downloads/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	mva@FreeBSD.org
COMMENT=	Dynamic Scripting for adaptive AI systems

LICENSE=	ZLIB

USE_PYTHON=	yes
USE_PYDISTUTILS=yes
PYDISTUTILS_AUTOPLIST=	yes

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

post-install:
.if ${PORT_OPTIONS:MDOCS}
	@${INSTALL} -d ${STAGEDIR}${DOCSDIR}/html
	@${TAR} -C ${WRKSRC}/doc/html -cf - . | \
		${TAR} -C ${STAGEDIR}${DOCSDIR}/html -xf -
.endif

.include <bsd.port.mk>
