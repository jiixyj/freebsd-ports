# Created by: Mark Pulford <mark@kyne.com.au>
# $FreeBSD$

PORTNAME=	penguin-command
PORTVERSION=	1.6.11
PORTREVISION=	8
CATEGORIES=	games
MASTER_SITES=	SF

MAINTAINER=	amdmi3@FreeBSD.org
COMMENT=	A clone of the classic game Missile Command

LIB_DEPENDS=	libpng.so:${PORTSDIR}/graphics/png \
		libjpeg.so:${PORTSDIR}/graphics/jpeg

USE_SDL=	mixer image sdl
GNU_CONFIGURE=	yes

PLIST_FILES=	bin/${PORTNAME} \
		man/man6/penguin-command.6.gz \
		man/man6/penguin-command.ja.6.gz
PORTDATA=	*

DESKTOP_ENTRIES="Penguin Command" \
		"${COMMENT}" \
		"${DATADIR}/gfx/icon.xpm" \
		"${PORTNAME}" \
		"Game;ArcadeGame;" \
		""

post-patch:
	@${REINPLACE_CMD} 's|LIBS="-lSDL_image|LIBS="-lSDL_image $$SDL_LIBS|g; \
		s| -lSDL | |g' ${WRKSRC}/configure

.include <bsd.port.mk>
