# Created by: Kimura Fuyuki <fuyuki@mj.0038.net>
# $FreeBSD$

PORTNAME=	resume
PORTVERSION=	1.5.1
PORTREVISION=	2
CATEGORIES=	textproc
MASTER_SITES=	SF/xml${PORTNAME}/xml${PORTNAME}/${PORTVERSION}
DISTNAME=	${PORTNAME}-${PORTVERSION:S/./_/g}
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	XML Resume library

USE_JAVA=	yes
NO_BUILD=	yes
PKGMESSAGE=	${WRKDIR}/pkg-message

.if !defined(NOPORTDOCS)
PORTDOCS=	*
.endif

NO_STAGE=	yes
post-patch:
	${REINPLACE_CMD} -e 's|\.\./\.\./css|css|' ${WRKSRC}/xsl/params.xsl
	${FIND} ${WRKSRC} -name '*.bak' -delete

do-install:
	${MKDIR} ${PREFIX}/share/xml/${PORTNAME}
	${CP} -R ${WRKSRC}/dtd/* ${PREFIX}/share/xml/${PORTNAME}
	${MKDIR} ${PREFIX}/share/xsl/${PORTNAME}
	${CP} -R ${WRKSRC}/xsl/* ${PREFIX}/share/xsl/${PORTNAME}
	${CP} -R ${WRKSRC}/css ${PREFIX}/share/xsl/${PORTNAME}/format
	${INSTALL_DATA} ${WRKSRC}/java/*.jar ${JAVAJARDIR}

post-install:
.if !defined(NOPORTDOCS)
	${MKDIR} ${EXAMPLESDIR}
	${CP} -R ${WRKSRC}/examples/* ${EXAMPLESDIR}
	${MKDIR} ${DOCSDIR}
	${CP} -R ${WRKSRC}/doc/* ${DOCSDIR}
.endif
	${SED} -e "s|%%PREFIX%%|${PREFIX}|g" pkg-message >${PKGMESSAGE}
	@${CAT} ${PKGMESSAGE}

.include <bsd.port.mk>
