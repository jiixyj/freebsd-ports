# Created by: jupengfei <jupengfei@gmail.com>
# $FreeBSD$

PORTNAME=	CPAN-Meta
PORTVERSION=	2.133380
CATEGORIES=	devel perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	The distribution metadata for a CPAN dist

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

BUILD_DEPENDS=	p5-CPAN-Meta-Requirements>=2.121:${PORTSDIR}/devel/p5-CPAN-Meta-Requirements \
		p5-CPAN-Meta-YAML>=0.008:${PORTSDIR}/devel/p5-CPAN-Meta-YAML \
		p5-Parse-CPAN-Meta>=1.44.03:${PORTSDIR}/devel/p5-Parse-CPAN-Meta \
		p5-Scalar-List-Utils>=1.33:${PORTSDIR}/lang/p5-Scalar-List-Utils
RUN_DEPENDS:=	${BUILD_DEPENDS}

USE_PERL5=	configure
USES=		perl5

.include <bsd.port.pre.mk>

.if ${PERL_LEVEL} < 501400
BUILD_DEPENDS+=	p5-version>=0.88:${PORTSDIR}/devel/p5-version
RUN_DEPENDS+=	p5-version>=0.88:${PORTSDIR}/devel/p5-version
.endif

.if ${PERL_LEVEL} < 501600
BUILD_DEPENDS+=	p5-JSON-PP>=2.27200:${PORTSDIR}/converters/p5-JSON-PP
RUN_DEPENDS+=	p5-JSON-PP>=2.27200:${PORTSDIR}/converters/p5-JSON-PP
.endif

.include <bsd.port.post.mk>
