# Created by: Peter Johnson <johnson.peter@gmail.com>
# $FreeBSD$

PORTNAME=	crx
PORTVERSION=	2.03
CATEGORIES=	devel
MASTER_SITES=	ftp://ftp.delorie.com/pub/djgpp/current/v2/ \
		ftp://ftp.mirror.ac.uk/sites/www.delorie.com/current/v2/ \
		http://djgpp.linux-mirror.org/v2/ \
		http://djgpp.oss-mirror.org/v2/
PKGNAMEPREFIX=	djgpp-
DISTNAME=	djcrx203

MAINTAINER=	johnson.peter@gmail.com
COMMENT=	Headers and Libraries for DJGPP cross-development

USE_ZIP=	yes
NO_MTREE=	yes
NO_WRKSUBDIR=	yes

NO_STAGE=	yes
post-extract:
	@${CP} ${FILESDIR}/Makefile ${WRKDIR}

.include <bsd.port.mk>
