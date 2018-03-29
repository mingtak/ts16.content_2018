# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ts16.content -t test_article.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ts16.content.testing.TS16_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_article.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Article
  Given a logged-in site administrator
    and an add article form
   When I type 'My Article' into the title field
    and I submit the form
   Then a article with the title 'My Article' has been created

Scenario: As a site administrator I can view a Article
  Given a logged-in site administrator
    and a article 'My Article'
   When I go to the article view
   Then I can see the article title 'My Article'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add article form
  Go To  ${PLONE_URL}/++add++Article

a article 'My Article'
  Create content  type=Article  id=my-article  title=My Article


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the article view
  Go To  ${PLONE_URL}/my-article
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a article with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the article title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
