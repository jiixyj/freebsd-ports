# Created by: roam@FreeBSD.org
# $FreeBSD$

PORTNAME=	timelimit
PORTVERSION=	1.8
PORTREVISION=	1
CATEGORIES=	sysutils
MASTER_SITES=	http://devel.ringlet.net/sysutils/timelimit/

MAINTAINER=	eadler@FreeBSD.org
COMMENT=	Limit the absolute execution time of a process

#LICENSE=	BSD - no proof

CONFLICTS=	netpipes-[0-9]*

PLIST_FILES=	bin/timelimit man/man1/timelimit.1.gz
NO_ARCH=	yes

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/timelimit ${STAGEDIR}${PREFIX}/bin
		${INSTALL_DATA} ${WRKSRC}/timelimit.1 ${STAGEDIR}${MAN1PREFIX}/man/man1/

.include <bsd.port.mk>
