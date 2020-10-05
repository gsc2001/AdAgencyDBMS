import subprocess as sp

from ..core import read, create, delete, update
from ..utils.createCLI import createCLI


def add_menu(connection, cursor):
    createCLI("ADD MENU", {
        'Actor': create.preAddActor,
        'Director': create.addDirector,
        'Brand': create.addBrand,
        'Channel': create.addChannel,
        'Show': create.addShow,
        'Product': create.addProduct,
        'Ad': create.addProduction,
        'Guardian': create.addGuardian
    }, connection, cursor, True)


def delete_menu(connection, cursor):
    createCLI("DELETE MENU", {
        'Actor': delete.deletePerson,
        'Director': delete.deletePerson,
        'Brand': delete.deleteBrand,
        'Channel': delete.deleteChannel,
        'Show': delete.deleteShow,
        'Product': delete.deleteProduct,
        'Ad': delete.deleteAd,
        'Guardian': delete.deleteGuardian
    }, connection, cursor, True)


def read_menu(connection, cursor):
    createCLI("READ MENU", {
        'Get all Actors': read.readActors,
        'Get all Directors': read.readDirectors,
        'Get all Brands': read.readBrands,
        'Get all Channels': read.readChannels,
        'Get all Shows': read.readShows,
        'Get all Products': read.readProducts,
        'Get all Ads': read.readAds,
        'Get all Guardians': read.getGuardians,
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
    createCLI("UPDATE MENU", {
        'Actor': actor_update_menu,
        'Director': director_update_menu,
        'Brand': brand_update_menu,
        'Product': product_update_menu,
        'Channel': channel_update_menu,
        'Show': show_update_menu,
        'Ad': ad_update_menu
    }, connection, cursor)


def actor_update_menu(connection, cursor):
    createCLI("ACTOR UPDATE MENU", {
        'AccountNumber': update.updateAccountNumber,
        'Name': update.updatePersonName,
        'Height and Weight': update.updateHeightWeight,
        'Add preffered brand': create.addPrefers,
        'Remove preffered brand': delete.deletePrefers
    }, connection, cursor, True)


def director_update_menu(connection, cursor):
    createCLI("DIRECTOR UPDATE MENU", {
        'AccountNumber': update.updateAccountNumber,
        'Name': update.updatePersonName,
        'Salary': update.updateSalary,
        'Supervisor': update.updateSupervisor
    }, connection, cursor, True)


def brand_update_menu(connection, cursor):
    createCLI("BRAND UPDATE MENU", {
        'POC Email': update.updateBrandEmail,
        'POC Phone': update.updateBrandPhone
    }, connection, cursor, True)


def product_update_menu(connection, cursor):
    createCLI("PRODUCT UPDATE MENU", {
        'Price': update.updateProductPrice,
        'Description': update.updateProductDescription
    }, connection, cursor, True)


def channel_update_menu(connection, cursor):
    createCLI("CHANNEL UPDATE MENU", {
        'Base Price': update.updateBasePrice
    }, connection, cursor, True)


def show_update_menu(connection, cursor):
    createCLI("SHOW UPDATE MENU", {
        'Surcharge': update.updateSurcharge,
        'Air an Ad': create.addAdinShow,
        'Remove an Ad': delete.deleteDisplayed
    }, connection, cursor, True)


def ad_update_menu(connection, cursor):
    createCLI("AD UPDATE MENU", {
        'Air in a show': create.addAdinShow,
        'Remove from a show': delete.deleteDisplayed
    }, connection, cursor, True)
