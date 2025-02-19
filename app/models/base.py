from app.extensions import db
import datetime

# Base Table
class Base(db.Model):

    #id
    id = db.Column(db.Integer, primary_key=True)
    #collection_id
    collection_id = db.Column(db.String(255),unique=True)
    #Objecttyp Name
    objecttype_name = db.Column(db.String(255))
    #Collection
    collection = db.Column(db.String(255))
    #Institution
    institution = db.Column(db.String(255))
    #Type:Status
    type_status = db.Column(db.String(255))
    #Total
    total = db.Column(db.String(255))
    #Name
    name = db.Column(db.String(255))
    #Gathering
    gathering = db.Column(db.String(255))
    #Name of Collector
    name_of_collector = db.Column(db.String(255))
    #Date of Collection
    date_of_collection = db.Column(db.String(255))
    #Remarks
    remarks = db.Column(db.String(255))

    #Taxonomic Variables

    #Subphylum
    subphylum = db.Column(db.String(255))
    #Class
    class_ = db.Column(db.String(255))
    #Order
    order = db.Column(db.String(255))
    #Family
    family = db.Column(db.String(255))
    #Genus
    genus = db.Column(db.String(255))
    #Subgenus
    subgenus = db.Column(db.String(255))
    #Species
    species = db.Column(db.String(255))
    #Subspecies
    subspecies = db.Column(db.String(255))

    #Publication Variables

    #Author
    author = db.Column(db.String(255))
    #Publication date
    publication_date = db.Column(db.String(255))
    #Reference
    reference = db.Column(db.String(255))
    #Link
    link = db.Column(db.String(255))
    #Status Name
    status_name = db.Column(db.String(255))
    #LSID
    lsid = db.Column(db.String(255))
    #Type:Kind
    type_kind = db.Column(db.String(255))

    #Collection Variables
    
    #Number of Individuals
    number_of_individuals = db.Column(db.Float(255))
    #Individual Status (...38)
    individual_status = db.Column(db.String(255))
    #Sex
    number_of_females = db.Column(db.Float(255))
    number_of_males = db.Column(db.Float(255))
    #Developmental Stage
    developmental_stage = db.Column(db.String(255))
    #Associated Object
    associated_object = db.Column(db.String(255))
    #Biographical Region
    biographical_region = db.Column(db.String(255))
    #Country
    country = db.Column(db.String(255))
    #Region
    region = db.Column(db.String(255))
    #Name Town
    name_town = db.Column(db.String(255))
    #Town_ID
    town_id = db.Column(db.String(255))
    #Latitude
    latitude = db.Column(db.String(255))
    #Longitude
    longitude = db.Column(db.String(255))
    #Elevation
    elevation = db.Column(db.String(255))
    #Habitat
    habitat = db.Column(db.String(255))