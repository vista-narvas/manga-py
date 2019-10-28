from argparse import ArgumentParser

from manga_py.meta import __version__


def _image_args(args_parser):  # pragma: no cover
    args = args_parser.add_argument_group('Image options')

    args.add_argument('--not-change-files-extension', action='store_const',
                      help='Save downloaded files to archive "as is". Default value: %(default)s.', const=True, default=False)

    # args.add_argument('--force-png', action='store_const',
    #                          help='Force conversation images to png format', const=True, default=False)
    # args.add_argument('--force-jpg', action='store_const',
    #                          help='Force conversation images to jpg format', const=True, default=False)
    args.add_argument('--no-webp', action='store_const', const=True, default=False,
                      help='Convert `*.webp` images to `*.jpg` format. Default value: %(default)s.')

    # args.add_argument('-xt', type=int, help='Manual image crop with top side', default=0)
    # args.add_argument('-xr', type=int, help='Manual image crop with right side', default=0)
    # args.add_argument('-xb', type=int, help='Manual image crop with bottom side', default=0)
    # args.add_argument('-xl', type=int, help='Manual image crop with left side', default=0)
    # args.add_argument('--crop-blank', action='store_const', help='Crop white lines on image',
    #                          const=True, default=False)


def _debug_args(args_parser):  # pragma: no cover
    args = args_parser.add_argument_group('Debug / Simulation options')

    args.add_argument('-h', '--help', action='help', help='Show (this) help and exit.')
    args.add_argument('--print-json', action='store_const', const=True, default=False, help='Print information about the results in the JSON format (after completion). Default value: %(default)s.')

    args.add_argument('--simulate', action='store_const', const=True, default=False,
            help='Simulate running Manga-py, where: 1) do not download files and, 2) do not write anything on disk. Default value: %(default)s.')

    args.add_argument('--show-current-chapter-info', '-cc', action='store_const', const=True, default=False,
                      help='Show current processing chapter info. Default value: %(default)s.')

    # args.add_argument('--full-error', action='store_const', const=True, default=False,
    #                   help='Show full stack trace')

    # args.add_argument('-vv', '--log', metavar='info', type='str', help='Verbose log')

    args.add_argument('--debug', action='store_true', help='Debug Manga-py.')


def _downloading_args(args_parser):  # pragma: no cover
    args = args_parser.add_argument_group('Downloading options')

    # args.add_argument('-U', '--update-all', action='store_const',
    #                   help='Update all. Not worked now!', const=True, default=False)
    args.add_argument('-s', '--skip-volumes', metavar='COUNT', type=int,
                      help='Skip a total number, i.e. %(metavar)s, of volumes. Default value: %(default)s.', default=0)
    args.add_argument('-c', '--max-volumes', metavar='COUNT', type=int,
            help='Download a maximum number, i.e. %(metavar)s, of volumes. E.g.: `--max-volumes 2` will download at most 2 volumes. If %(metavar)s is `0` (zero) then it will download all avaliable volumes. Default value: %(default)s.', default=0)
    args.add_argument('--user-agent', type=str, help='Set an user-agent. Don\'t work from protected sites. Default value: %(default)s.')
    args.add_argument('--proxy', type=str, help='Set a http proxy. Default value: %(default)s.')
    args.add_argument('--reverse-downloading', action='store_const',
                      help='Download manga volumes in a reverse order. By default, the manga will be downloaded in a ascendent order (i.e. volume 00, volume 01, volume 02...). If `--reverse-downloading` has been actived, then the manga will be downloaded in a descendent order (i.e. volume 99, volume 98, volume 97...). Default value: %(default)s.', const=True, default=False)
    args.add_argument('--rewrite-exists-archives', action='store_const', help='(Re)Download manga volume if it already exists locally in the directory destination. Your manga files can be overwrited, so be careful. Default value: %(default)s.', const=True, default=False)
    args.add_argument('-nm', '--max-threads', type=int, help='Set the maximum number of threads, i.e. MAX_THREADS, to be ready to use when downloading the manga images. Default value: %(default)s.', default=None)
    args.add_argument('--zero-fill', action='store_const', const=True, default=False,
                      help='Pad a `-0` (dash-and-zero) at right for all downloaded manga volume filenames. E.g. from `vol_001.zip` to `vol_001-0.zip`. It is useful to standardize the filenames between normal manga volumes (e.g. vol_006.zip) and the extra/bonuses/updated/corrected manga volumes (e.g. vol_006-5.zip) released by scanlators groups. Default value: %(default)s.')
    args.add_argument('-N', '--with-manga-name', action='store_const', const=True, default=False,
                      help='Pad the manga name at left for all downloaded manga volumes filenames. E.g. from `vol_001.zip` to `manga_name-vol_001.zip`. Default value: %(default)s.')
    args.add_argument('--min-free-space', metavar='MB', type=int,
                      help='Alert when the minimum free disc space, i.e. MB, is reached. Insert it in order of megabytes (Mb). Default value: %(default)s.', default=100)


def _reader_args(args_parser):  # pragma: no cover
    args = args_parser.add_argument_group('Archive options')

    args.add_argument('--cbz', action='store_const', default=False,
                      const=True, help='Make `*.cbz` archives (for reader). Default value: %(default)s.')

    args.add_argument('--rename-pages', action='store_const', default=False, const=True,
                      help='Normalize image filenames. E.g. from `0_page_1.jpg` to `0001.jpg`. Default value: %(default)s.')


def get_cli_arguments() -> ArgumentParser:  # pragma: no cover
    args_parser = ArgumentParser(add_help=False)
    args = args_parser.add_argument_group('General options')

    args.add_argument('url', metavar='URL', type=str, help='%(metavar)s, i.e. link from manga, to be downloaded.')
    args.add_argument('--version', action='version', version=__version__, help='Show Manga-py\'s version number and exit.')

    args.add_argument('-n', '--name', metavar='NAME', type=str, help='Rename manga, i.e. by %(metavar)s, and its folder to where it will be saved locally. Default value: %(default)s.', default='')
    args.add_argument('-d', '--destination', metavar='PATH', type=str,
            help='Destination folder to where the manga will be saved locally, i.e. `./%(metavar)s/manga_name/`. E.g.: `./%(default)s/manga_name/` or `./FOO/manga_name/`. Default value: %(default)s.', default='Manga')
    args.add_argument('-np', '--no-progress', metavar='no-progress', action='store_const',
                      const=True, help='Don\'t show progress bar. Default value: %(default)s', default=False)
    # future
    # args_parser.add_argument('--server', action='store_const', const=True, help='Run web interface',
    #                          default=False)

    _image_args(args_parser)
    _reader_args(args_parser)
    _downloading_args(args_parser)
    _debug_args(args_parser)

    return args_parser
