# Created by: Alexey Dokuchaev <danfe@regency.nsu.ru>
# $FreeBSD$

PORTNAME=	wmwork
PORTVERSION=	0.2.5
PORTREVISION=	3
CATEGORIES=	misc windowmaker afterstep
MASTER_SITES=	http://people.debian.org/~godisch/wmwork/ \
		${MASTER_SITE_LOCAL}
MASTER_SITE_SUBDIR=	xride

MAINTAINER=	xride@FreeBSD.org
COMMENT=	A dockapp that keeps track of time you have spent on something

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}/src

USE_XORG=	xpm
USE_GMAKE=	yes
GNU_CONFIGURE=	yes

MAN1=		wmwork.1
PLIST_FILES=	bin/wmwork

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

NO_STAGE=	yes
do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/wmwork ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/wmwork.1 ${MANPREFIX}/man/man1

.include <bsd.port.mk>
