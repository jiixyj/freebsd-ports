# Created by: Denis Shaposhnikov <dsh@vlink.ru>
# $FreeBSD$

PORTNAME=	qlas
PORTVERSION=	1.93
CATEGORIES=	misc
MASTER_SITES=	http://lev.serebryakov.spb.ru/download/qlas/

MAINTAINER=	dsh@vlink.ru
COMMENT=	Qico FIDO mailer log analyzer and statistic builder

NO_WRKSUBDIR=	yes
NO_BUILD=	yes
USES=		shebangfix perl5
SHEBANG_FILES=	qlas
USE_DOS2UNIX=	qlas qlas.conf.default

NO_STAGE=	yes
do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/qlas ${PREFIX}/bin/
	${INSTALL_DATA} ${WRKSRC}/qlas.conf.default ${PREFIX}/etc/

.include <bsd.port.mk>
