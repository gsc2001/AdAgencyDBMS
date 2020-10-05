import subprocess as sp

from ..core import read, create, delete, update
from ..utils.createMenu import createMenu


def add_menu(connection, cursor):
    createMenu("ADD MENU", {
        'Actor': create.addActor,
        'Director': create.addDirector,
        'Brand': create.addBrand,
        'Channel': create.addChannel,
        'Show': create.addShow,
        'Product': create.addProduct,
        'Ad': create.addProduction,
        'Gaurdian': create.addGaurdian
    }, connection, cursor, True)


def delete_menu(connection, cursor):
    createMenu("DELETE MENU", {
        'Actor': delete.deletePerson,
        'Director': delete.deletePerson,
        'Brand': delete.deleteBrand,
        'Channel': delete.deleteChannel,
        'Show': delete.deleteShow,
        'Product': delete.deleteProduct,
        'Ad': delete.deleteAd,
        'Gaurdian': delete.deleteGuardian
    }, connection, cursor, True)


def read_menu(connection, cursor):
    createMenu("READ MENU", {
        'Get all Actors': read.readActors,
        'Get all Directors': read.readDirectors,
        'Get all Brands': read.readBrands,
        'Get all Channels': read.readChannels,
        'Get all Shows': read.readShows,
        'Get all Products': read.readProducts,
        'Get all Ads': read.readAds,
        'Get all Gaurdians': read.getGuardians,
        'Get Ad-Show Relations': read.getAdShows,
        "Get Actor's preffered brands": read.getActorBrands,
        "Actors with Physical features": read.actorsByFeatures,
        'Average ad production cost': read.avgProduction,
        "Maximum preferred brands": read.maxPreferred,
        'Partial text search for shows': read.searchShow,
        'Partial text search for actor': read.searchActor,
        'Get best shows for an ad': read.showsForAd,
        'Shows with surcharge less than a value': read.surchargeLessThan,
        'Maximum of sum of the contract money of brand': read.maxProdCost,
        'Bill for an Ad': read.adBill,
        'Shows list by amount': read.showList
    }, connection, cursor, True)


def update_menu(connection, cursor):
    createMenu("UPDATE MENU", {
        'Actor': actor_update_menu,
        'Director': director_update_menu
    }, connection, cursor)


def actor_update_menu(connection, cursor):
    createMenu("ACTOR UPDATE MENU", {
        'AccountNumber': update.updateAccountNumber,
        'Name': update.updatePersonName,
        'Height and Weight': update.updateHeightWeight,
        'Add preffered brand': create.addPrefers,
        'Remove preffered brand': delete.deletePrefers
    }, connection, cursor, True)


def director_update_menu(connection, cursor):
    createMenu("DIRECTOR UPDATE MENU", {
        'AccountNumber': update.updateAccountNumber,
        'Name': update.updatePersonName,
        'Salary': update.updateSalary,
        'Supervisor': update.updateSupervisor
    }, connection, cursor, True)
