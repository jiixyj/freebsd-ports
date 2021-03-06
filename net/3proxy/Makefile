# Created by: tim@relay.nnn.tstu.ru
# $FreeBSD$

PORTNAME=	3proxy
PORTVERSION=	0.6.1
CATEGORIES=	net
MASTER_SITES=	http://3proxy.ru/${PORTVERSION}/ \
		http://security.nnov.ru/soft/3proxy/${PORTVERSION}/
EXTRACT_SUFX=	.tgz

MAINTAINER=	osa@FreeBSD.org
COMMENT=	Proxy servers set (support HTTP(S), FTP, SOCKS, POP3, TCP & UDP)

CONFLICTS=	libproxy-[0-9]*

USE_RC_SUBR=	3proxy
MAKEFILE=	Makefile.unix
MAKE_ENV=	PTHREAD_LIBS="${PTHREAD_LIBS}" \
		PTHREAD_CFLAGS="${PTHREAD_CFLAGS}"

MAN3=	3proxy.cfg.3
MAN8=	3proxy.8 ftppr.8 pop3p.8 proxy.8 socks.8 tcppm.8 udppm.8

NO_STAGE=	yes
post-patch:
	${REINPLACE_CMD} -e "s|%%CFLAGS%%|${CFLAGS}|" \
		${WRKSRC}/Makefile.unix

do-install:
	${MKDIR} ${PREFIX}/lib/${PORTNAME}
.for i in 3proxy countersutil dighosts ftppr icqpr msnpr \
	mycrypt pop3p proxy smtpp socks tcppm udppm
	${INSTALL_PROGRAM} ${WRKSRC}/src/${i} ${PREFIX}/bin/
.endfor
.for p in PCREPlugin.so StringsPlugin.so TrafficPlugin.so
	${INSTALL_PROGRAM} ${WRKSRC}/src/${p} ${PREFIX}/lib/${PORTNAME}
.endfor
	${INSTALL_DATA} ${WRKSRC}/cfg/3proxy.cfg.sample ${PREFIX}/etc
	${INSTALL_MAN} ${WRKSRC}/man/${MAN3} ${PREFIX}/man/man3
.for i in ${MAN8}
	${INSTALL_MAN} ${WRKSRC}/man/${i} ${PREFIX}/man/man8
.endfor

post-install:
.if !defined(NOPORTDOCS)
	${MKDIR} ${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/Readme ${DOCSDIR}
.endif

.include <bsd.port.mk>
