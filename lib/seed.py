#!/usr/bin/env python3

# Script goes here!

from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


Facebook = Company(name="Facebook", founding_year=2004)
Uber = Company(name="Uber", founding_year=2009)

Mary = Dev(name="Mary")
Machuma = Dev(name="Machuma")

freebie1 = Freebie(item_name="Scholarship", value=500, company=Facebook, dev=Mary)
freebie2 = Freebie(item_name="Free rides", value=100, company=Uber, dev=Machuma)
freebie3 = Freebie(item_name="T-SHIRT", value=2, company=Facebook, dev=Mary)

session.add_all([Facebook, Uber, Mary, Machuma, freebie1, freebie2, freebie3])
session.commit()