from api.cassiopeia.cassiopeia import riotapi

def main():
    # Setup riotapi
    riotapi.set_region("NA")
    riotapi.print_calls(True)
    key = 'b7190b84-484d-4cc7-88ca-8e2b90fb7f56'  # You can create an env var called "DEV_KEY" that holds your developer key. It will be loaded here.
    riotapi.set_api_key(key)

    games = riotapi.get_featured_games()

    print games



if __name__ == "__main__":
    main()