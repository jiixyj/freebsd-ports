# $FreeBSD$

PORTNAME=	HTTP-Session2
PORTVERSION=	0.04
CATEGORIES=	www perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	kuriyama@FreeBSD.org
COMMENT=	Perl extension for HTTP session management

RUN_DEPENDS=	\
	p5-Cookie-Baker>0:${PORTSDIR}/www/p5-Cookie-Baker \
	p5-Digest-HMAC>0:${PORTSDIR}/security/p5-Digest-HMAC \
	p5-Digest-SHA1>0:${PORTSDIR}/security/p5-Digest-SHA1 \
	p5-Mouse>0:${PORTSDIR}/devel/p5-Mouse
BUILD_DEPENDS=	${RUN_DEPENDS}

USES=		perl5
USE_PERL5=	modbuild

.include <bsd.port.mk>
