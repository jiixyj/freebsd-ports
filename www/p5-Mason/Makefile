# Created by: Muhammad Moinur Rahman <5u623l20@gmail.com>
# $FreeBSD$

PORTNAME=	Mason
PORTVERSION=	2.20
CATEGORIES=	www textproc perl5
MASTER_SITES=	CPAN
MASTER_SITE_SUBDIR=	CPAN:JSWARTZ
PKGNAMEPREFIX=	p5-

MAINTAINER=	5u623l20@gmail.com
COMMENT=	High-performance, dynamic web site authoring system

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-Capture-Tiny>=0:${PORTSDIR}/devel/p5-Capture-Tiny \
		p5-Class-Unload>=0:${PORTSDIR}/devel/p5-Class-Unload \
		p5-Devel-GlobalDestruction>=0:${PORTSDIR}/devel/p5-Devel-GlobalDestruction \
		p5-Exception-Class>=0:${PORTSDIR}/devel/p5-Exception-Class \
		p5-Guard>=0:${PORTSDIR}/devel/p5-Guard \
		p5-IPC-System-Simple>=0:${PORTSDIR}/devel/p5-IPC-System-Simple \
		p5-JSON>=0:${PORTSDIR}/converters/p5-JSON \
		p5-Log-Any>=0.08:${PORTSDIR}/devel/p5-Log-Any \
		p5-Method-Signatures-Simple>=0:${PORTSDIR}/devel/p5-Method-Signatures-Simple \
		p5-Moose>=1.15:${PORTSDIR}/devel/p5-Moose \
		p5-MooseX-HasDefaults>=0.03:${PORTSDIR}/devel/p5-MooseX-HasDefaults \
		p5-MooseX-StrictConstructor>=0.13:${PORTSDIR}/devel/p5-MooseX-StrictConstructor \
		p5-Try-Tiny>=0:${PORTSDIR}/lang/p5-Try-Tiny
RUN_DEPENDS:=	${BUILD_DEPENDS}
TEST_DEPENDS=	p5-Test-Class-Most>=0:${PORTSDIR}/devel/p5-Test-Class-Most \
		p5-Test-LongString>=0:${PORTSDIR}/devel/p5-Test-LongString

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.mk>
