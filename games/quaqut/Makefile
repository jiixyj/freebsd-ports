# Created by: Alexander Logvinov <ports@logvinov.com>
# $FreeBSD$

PORTNAME=	quaqut
PORTVERSION=	0.2.0
CATEGORIES=	games
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}%20C%20sources/${PORTNAME}-${PORTVERSION}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Queries information from Unreal Tournament 2004 game servers


HAS_CONFIGURE=	yes
USE_RC_SUBR=	${PORTNAME}
MAN1=		${PORTNAME}.1
PORTDOCS=	AUTHORS COPYING ChangeLog README
PLIST_FILES=	bin/${PORTNAME}

NO_STAGE=	yes
do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/${PORTNAME} ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/${MAN1} ${MAN1PREFIX}/man/man1
.if !defined(NOPORTDOCS)
	@${MKDIR} ${DOCSDIR}
.for i in ${PORTDOCS}
	${INSTALL_DATA} ${WRKSRC}/${i} ${DOCSDIR}
.endfor
.endif

.include <bsd.port.mk>
