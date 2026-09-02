import numpy as np

from sklearn.neighbors import BallTree

from config import EARTH_RADIUS_KM


def build_spatial_tree(
    properties_df
):

    coordinates = np.radians(
        properties_df[
            [
                "lat",
                "long",
            ]
        ].to_numpy()
    )

    return BallTree(
        coordinates,
        metric="haversine",
    )


def find_neighbors(
    properties_df,
    latitude,
    longitude,
    n_neighbors=10,
):

    if len(properties_df) == 0:
        return properties_df.copy()

    tree = build_spatial_tree(
        properties_df
    )

    query = np.radians(
        np.array(
            [
                [
                    latitude,
                    longitude,
                ]
            ]
        )
    )

    k = min(
        n_neighbors + 1,
        len(properties_df),
    )

    distances, indices = tree.query(
        query,
        k=k,
    )

    neighbors = (
        properties_df
        .iloc[
            indices[0]
        ]
        .copy()
        .reset_index(drop=True)
    )

    neighbors[
        "distance_km"
    ] = (
        distances[0]
        * EARTH_RADIUS_KM
    )

    # Remove the selected property
    # when the query matches an existing property.
    neighbors = neighbors[
        ~(
            np.isclose(
                neighbors["lat"],
                latitude
            )
            &
            np.isclose(
                neighbors["long"],
                longitude
            )
        )
    ]

    return (
        neighbors
        .head(n_neighbors)
        .reset_index(drop=True)
    )