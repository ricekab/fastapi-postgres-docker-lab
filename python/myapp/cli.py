""" CLI for managing database tables and seeding data. """
import os
import sys
from argparse import ArgumentParser

import click
from sqlalchemy.orm import Session

from myapp import db
from myapp.model import Airport


@click.group(help="CLI to manage DB tables.")
def cli():
    """ CLI main """
    pass


@cli.group(name='airport',
           help='Manage airport entries')
def airport_cli():
    pass


@airport_cli.command(name='create')
@click.option('--icao', type=str, required=True)
@click.option('--name', type=str, required=True)
def airport_create(icao, name):
    airport = Airport(icao=icao, name=name)
    with Session(db.get_engine()) as session:
        session.add(airport)
        session.commit()


@cli.group(name='db',
           help='DB table management')
def db_cli():
    pass


@db_cli.command(name='create')
def db_create():
    db.create_tables()


@db_cli.command(name='drop')
def db_drop():
    db.drop_tables()


@db_cli.command(name='renew')
def db_renew():
    db.renew_tables()


if __name__ == '__main__':
    cli()
