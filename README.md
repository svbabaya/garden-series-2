# garden-series-2
Web content of the project Garden. Part 2. School number 30.

ToThink
1. Does it need to add serial number of article to the model Article?

ToDo
1. Fix REST API and review best practise
2. Add migrations
3. Add export db to json
4. Add exceptions (db, json, images)
5. Add Flask_upload for files
OK 6. Add settings.json
7. Make sceme of models in README (mermaid)
8. Make Logo active (Go home)
9. Add modal window for Archive feature

OK 9. Make buttons for categories on index.html
10. Make design index.html

OK 12. Add number of plants in the each cathegory (index.html and cathegory.html)

13. Make functions CRUD (get all plants, get cathegory plants, get one plant, create plant, create article, delete plant, delete article, update plant, update article)

OK Create message, read messages, delete message, patch message

14. Add localization

15. Add function for messages (priority handle)
8. Add Duration attribute in Message model
8. To Think: Add expired time for news and absolute messages in model

OK 16. Make map, add pulse spot (video)
18. Add container for whole site (limit the width of site)
19. Correct footer bg image (thin lines, whithout shadows, svg)
20. To Think: How to make spot in location.html for iOS Safary (Fix problem with video webm on iOS)

OK 21. Make common template base.html and two templates: admin_base.html, view_base.html




        "articles": 
        [
            {
                "text": "Article text",
                "photo": "",
                "composition": "",
                "display": "",
                "plant_id": "",
                "status": "CREATED",
                "timestamp": "2025-04-21 22:09:40.814250"
            }
        ]

Design:
1. Growing picture of plant - tree, tree with fruits, bush with flowers, berries etc (Change ones per day, week)
2. Change icons of main buttons random (leaf, berry, flower, seed, butterfly, dragonfly, bird)
3. Add menu About Us, About Garden (Garden History), Plant List (List of all plants, Search (text))
4. Add information in footer
5. To Think: Design for wide screen, desktop
6. Add button Share on the card
7. Use QR code for plants (in admin generate QR image and send to email)

OK 8. Add floating button Top in category.html


Information about plants:
1. Approve the catalog and numbers of the categories
2. Create and approve rules of making for articles and messages
3. Finish the map of location, make coordinate grid and positions in pixels (add to enum Location)
4. Make the story of the garden
5. Start to make texts about plants in DOC format
6. Make photos in the garden (in summer)
7. Add very rare or very unordinary plants from all over the world
8. Add inexistent plants from tales and fantastic stories

Messages:
1. Phrase (normal)
2. Poetry (normal)
3. Puzzles
3. Advert about garden from gardener
4. Advert about school from teacher
5. News about garden (add new plant, correct mistake)
6. Сongratulation of someone
7. Hot news (high priority)
