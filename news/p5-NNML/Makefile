# Created by: Gea-Suan Lin <gslin@gslin.org>
# $FreeBSD$

PORTNAME=	NNML
PORTVERSION=	1.14
CATEGORIES=	news perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	gslin@gslin.org
COMMENT=	A minimal NNTP server

USES=		perl5
USE_PERL5=	configure

RESTRICTED=	License unknown

MAN1=		nnmirror.1 nnsync.1 overview.1
MAN3=		NNML::Server.3

.if defined(BATCH)
CONFIGURE_ARGS+=	< /dev/null
.else
IS_INTERACTIVE=	yes
.endif

NO_STAGE=	yes
.include <bsd.port.mk>
