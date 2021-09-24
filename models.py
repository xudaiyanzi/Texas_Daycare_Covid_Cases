import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_name = os.getenv('DB_NAME','covid_in_tx_daycare')
database_host = os.getenv('DB_HOST', 'localhost:5432')
database_path = "postgresql://{}/{}".format(database_host, database_name)

db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Covid_in_tx_daycare

'''
class Covid_in_tx_daycare(db.Model):  
  __tablename__ = 'covid_in_tx_daycare'

  id = Column(Integer, primary_key=True)
  county = Column(String)
  child_care_name = Column(String)
  street_address = Column(String)
  city = Column(String)
  zip = Column(String)
  kid_count_covid_on_09202021 = Column(Integer)
  staff_count_covid_on_09202021 = Column(Integer)
  kid_total_count_covid_since_052021 = Column(Integer)
  staff_total_count_covid_since_052021 = Column(Integer)

  def __init__(self, county, child_care_name, street_address, city,\
    zip,kid_count_covid_on_09202021,staff_count_covid_on_09202021,\
    kid_total_count_covid_since_052021, staff_total_count_covid_since_052021):

    self.county = county
    self.child_care_name = child_care_name
    self.street_address = street_address
    self.zip = zip
    self.kid_count_covid_on_09202021 = kid_count_covid_on_09202021
    self.staff_count_covid_on_09202021 = staff_count_covid_on_09202021
    self.kid_total_count_covid_since_052021 = kid_total_count_covid_since_052021
    self.staff_total_count_covid_since_052021 = staff_total_count_covid_since_052021

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'county': self.county,
      'child_care_name': self.child_care_name,
      'street_address': self.street_address,
      'city': self.city,
      'zip': self.zip,
      'kid_count_covid_on_09202021': self.kid_count_covid_on_09202021,
      'staff_count_covid_on_09202021': self.staff_count_covid_on_09202021,
      'kid_total_count_covid_since_052021': self.kid_total_count_covid_since_052021,
      'staff_total_count_covid_since_052021': self.staff_total_count_covid_since_052021
    }