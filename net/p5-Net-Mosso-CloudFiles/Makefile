# Created by: glarkin
# $FreeBSD$

PORTNAME=	Net-Mosso-CloudFiles
PORTVERSION=	0.44
CATEGORIES=	net perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Perl interface to the Mosso CloudFiles service

RUN_DEPENDS=	p5-Digest-MD5-File>=0:${PORTSDIR}/security/p5-Digest-MD5-File \
		p5-Moose>=0:${PORTSDIR}/devel/p5-Moose \
		p5-MooseX-StrictConstructor>=0:${PORTSDIR}/devel/p5-MooseX-StrictConstructor \
		p5-libwww>=0:${PORTSDIR}/www/p5-libwww \
		p5-LWP-UserAgent-Determined>=0:${PORTSDIR}/www/p5-LWP-UserAgent-Determined \
		p5-Data-Stream-Bulk>=0:${PORTSDIR}/devel/p5-Data-Stream-Bulk \
		p5-LWP-ConnCache-MaxKeepAliveRequests>=0:${PORTSDIR}/www/p5-LWP-ConnCache-MaxKeepAliveRequests \
		p5-JSON-XS-VersionOneAndTwo>=0:${PORTSDIR}/converters/p5-JSON-XS-VersionOneAndTwo \
		p5-DateTime-Format-HTTP>=0:${PORTSDIR}/devel/p5-DateTime-Format-HTTP \
		p5-Crypt-SSLeay>=0:${PORTSDIR}/security/p5-Crypt-SSLeay \
		p5-File-Slurp>=0:${PORTSDIR}/devel/p5-File-Slurp
BUILD_DEPENDS:=	${RUN_DEPENDS}
TEST_DEPENDS=	p5-Test-Exception>=0:${PORTSDIR}/devel/p5-Test-Exception

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
