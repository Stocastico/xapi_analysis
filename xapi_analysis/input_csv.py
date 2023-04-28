# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_input_csv.ipynb.

# %% auto 0
__all__ = ['get_all_verbs', 'get_all_actors', 'get_all_objects', 'remove_whitespaces', 'to_lowercase', 'remove_actors',
           'remove_verbs', 'count_interactions', 'subset_actor_verb', 'split_column', 'average_interactions']

# %% ../nbs/01_input_csv.ipynb 10
def get_all_verbs(df: pd.DataFrame # The dataset containing the xAPI statements (one statement per row)
                 ) -> Set: # Set containing all the verbs occurring in the dataset
    """
    Returns a set with all verbs in the dataset
    """
    return set(df["verb"].unique())

# %% ../nbs/01_input_csv.ipynb 13
def get_all_actors(df: pd.DataFrame # The dataset containing the xAPI statements (one statement per row)
                 ) -> Set: # Set containing all the actors occurring in the dataset
    """
    Returns a set with all actors in the dataset
    """
    return set(df["actor"].unique())

# %% ../nbs/01_input_csv.ipynb 15
def get_all_objects(df: pd.DataFrame # The dataset containing the xAPI statements (one statement per row)
                 ) -> Set: # Set containing all the objects occurring in the dataset
    """
    Returns a set with all objects in the dataset
    """
    return set(df["object"].unique())

# %% ../nbs/01_input_csv.ipynb 17
def remove_whitespaces(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                       cols: List # the columns on which whitespaces should be removed
                      ) -> pd.DataFrame: # The dataframe after applying the function
    """
    Removes whitespaces from the specified columns in the dataframe.
    """
    df[cols] = df[cols].apply(lambda s : s.str.replace(" ", ""))
    return df

# %% ../nbs/01_input_csv.ipynb 18
def to_lowercase(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                       cols: List # the columns whose content should be made lowercase
                      ) -> pd.DataFrame: # The dataframe after applying the function
    """
    Converts to lowercase the elements in the specified columns.
    The function only applies to columnns whose type is *str*
    """
    df[cols] = df[cols].applymap(lambda s: s.lower() if type(s) == str else s)
    return df

# %% ../nbs/01_input_csv.ipynb 21
def remove_actors(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                       cols: List # the list of actors to remove
                      ) -> pd.DataFrame: # The dataframe with the specified actors removed
    """
    Removes from the dataframe all the rows whose actor is in the specified list
    """
    return df[~df['actor'].isin(cols)]

# %% ../nbs/01_input_csv.ipynb 23
def remove_verbs(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                       cols: List # the list of verbs to remove
                      ) -> pd.DataFrame: # The dataframe with the specified verbs removed
    """
    Removes from the dataframe all the rows whose actor is in the specified list
    """
    return df[~df['verb'].isin(cols)]

# %% ../nbs/01_input_csv.ipynb 28
def count_interactions(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                    ) -> pd.DataFrame: # A dataframe with the number of interactions of each actor
    """
    Creates a new dataframe counting the total number of statements associated to each actor
    """
    tmp = df.groupby(['actor'])["verb"].agg(['count']).sort_values("count")
    tmp.reset_index(inplace=True)
    return tmp

# %% ../nbs/01_input_csv.ipynb 33
def subset_actor_verb(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                      actor: str, # The actor we are interested in
                      verb: str # The verb we are interested in
                    ) -> pd.DataFrame: # A dataframe containing only the statements with a specific actor and verb
    """
    Returns the subset of the original dataframe containing only statements with the specified actor and verb
    """
    return df[(df["actor"]==actor) & (df["verb"]==verb)]

# %% ../nbs/01_input_csv.ipynb 36
def split_column(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                 col: str, # The column in the dataset that should be split into multiple columns
                 col_names: List, # The names of the columns created after split
                 sep: str =';', # The separator between fiels inside the column we want to split
                ) -> pd.DataFrame: # A dataframe with the content *col* cplit into several columns 
    """
    Splits the column of the DataFrame into multiple columns, and return a new data
    """
    new_df = df[col].str.split(sep, expand=True)
    if len(new_df.columns) == len(col_names):
        new_df.columns = col_names
        return new_df
    else:
        print("The length of col_names should match the number of generated columns")
        return pd.DataFrame()

# %% ../nbs/01_input_csv.ipynb 38
def average_interactions(df: pd.DataFrame, # The dataset containing the xAPI statements (one statement per row)
                         avg_col: str, # The column on which to compute average
                         user_col: str = 'actor' # The column to groupby (usually **actor**)
                    ) -> pd.DataFrame: # A new dataframe with the average of the interaction per specific value
    """
    Similar to `count_interactions`, but here creates a new dataframe averaging the statements
    associated to a specific column
    """
    new_df = df.groupby(user_col, as_index=False)[avg_col].mean().sort_values(avg_col)
    return new_df
