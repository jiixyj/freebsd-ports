# Created by: Leland Wang <llwang@infor.org>
# $FreeBSD$

PORTNAME=	fbbi
PORTVERSION=	2003.0326
PORTREVISION=	1
CATEGORIES=	lang
MASTER_SITES=	http://www3.telus.net/public/cpressey/distfiles/
EXTRACT_SUFX=	.tgz

MAINTAINER=	ports@FreeBSD.org
COMMENT=	An interpreter for the Befunge-98 language

PLIST_FILES=	bin/fbbi
USE_GMAKE=	yes

WRKSRC=		${WRKDIR}/${DISTNAME}/src

post-patch:	.SILENT
	${REINPLACE_CMD} -e '/^CC/s/=/?=/' \
		-e '/^CFLAGS/{s/=/+=/;s/-g//;s/-O//;}' \
		${WRKSRC}/Makefile

NO_STAGE=	yes
do-install:
	@${INSTALL_PROGRAM} ${WRKSRC}/../bin/fbbi ${PREFIX}/bin

.include <bsd.port.mk>
